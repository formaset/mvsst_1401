from django.core.paginator import Paginator
from django.db import models
from django.utils import timezone
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.images import get_image_model_string
from wagtail.search import index

from .blocks import (
    CalloutBlock,
    DividerBlock,
    GalleryBlock,
    ImageBlock,
    KeyNumberBlock,
    QuoteBlock,
    VideoBlock,
)
from wagtail import blocks


class NewsIndexPage(Page):
    template = "news/news_index_page.html"
    subpage_types = ["news.NewsPage"]
    parent_page_types = ["core.HomePage"]

    intro = models.TextField(blank=True, verbose_name="Вступление")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        news_items = (
            NewsPage.objects.child_of(self)
            .live()
            .order_by("-date")
        )
        paginator = Paginator(news_items, 6)
        page_number = request.GET.get("page")
        context["news_page_obj"] = paginator.get_page(page_number)
        return context

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class NewsPage(Page):
    template = "news/news_page.html"
    parent_page_types = ["news.NewsIndexPage"]

    date = models.DateField(default=timezone.now, verbose_name="Дата публикации")
    intro = models.CharField(max_length=255, verbose_name="Краткий лид")
    cover_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="news_cover",
        verbose_name="Обложка",
    )
    body = StreamField(
        [
            ("paragraph", blocks.RichTextBlock(label="Абзац")),
            ("heading", blocks.CharBlock(label="Заголовок")),
            ("image", ImageBlock()),
            ("video", VideoBlock()),
            ("quote", QuoteBlock()),
            ("callout", CalloutBlock()),
            ("divider", DividerBlock()),
            ("key_number", KeyNumberBlock()),
            ("gallery", GalleryBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Контент",
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("cover_image"),
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField(\"intro\"),
        index.SearchField(\"body\"),
    ]

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
