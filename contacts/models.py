from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import format_html
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

ALLOWED_YANDEX_HOSTS = {
    "yandex.ru",
    "maps.yandex.ru",
    "yandex.com",
    "yandex.by",
    "yandex.kz",
    "yandex.com.tr",
    "yandex.uz",
}


def extract_iframe_src(value: str) -> str:
    if not value:
        return ""
    lower = value.lower()
    if "<iframe" in lower:
        start = lower.find("src=")
        if start == -1:
            return ""
        chunk = value[start + 4 :].lstrip()
        quote = chunk[0]
        if quote not in {"\"", "'"}:
            return ""
        end = chunk.find(quote, 1)
        return chunk[1:end] if end != -1 else ""
    return value.strip()


class ContactsPage(Page):
    template = "contacts/contacts_page.html"
    parent_page_types = ["core.HomePage"]

    phone = models.CharField(max_length=40, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    legal_address = models.CharField(max_length=255, verbose_name="Юридический адрес")
    actual_address = models.CharField(max_length=255, verbose_name="Фактический адрес")
    working_hours = models.CharField(
        max_length=255,
        verbose_name="График работы",
        default="ПН–ЧТ 08:00–17:00, ПТ 08:00–16:00, перерыв 12:00–13:00",
    )
    full_name = models.CharField(max_length=255, verbose_name="Полное наименование")
    short_name = models.CharField(max_length=255, verbose_name="Сокращённое наименование")
    map_embed = models.TextField(
        blank=True,
        verbose_name="Yandex Maps embed URL / iframe code",
        help_text="Вставьте ссылку или iframe-код. Разрешены домены yandex.*",
    )

    content_panels = Page.content_panels + [
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("legal_address"),
        FieldPanel("actual_address"),
        FieldPanel("working_hours"),
        FieldPanel("full_name"),
        FieldPanel("short_name"),
        FieldPanel("map_embed"),
    ]

    def clean(self):
        super().clean()
        if self.map_embed:
            embed_url = extract_iframe_src(self.map_embed)
            if not embed_url:
                raise ValidationError({"map_embed": "Не удалось извлечь ссылку из iframe."})
            parsed = urlparse(embed_url)
            host = parsed.netloc.split(":")[0]
            if host not in ALLOWED_YANDEX_HOSTS:
                raise ValidationError({"map_embed": "Разрешены только домены Yandex."})

    def map_iframe(self):
        embed_url = extract_iframe_src(self.map_embed)
        if not embed_url:
            return ""
        return format_html(
            '<iframe src="{}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
            embed_url,
        )

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
