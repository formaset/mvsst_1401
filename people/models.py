from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Leader(models.Model):
    name = models.CharField(max_length=120, verbose_name="ФИО")
    title = models.CharField(max_length=120, verbose_name="Должность")
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="leaders",
        verbose_name="Фото",
    )
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("photo"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"

    def __str__(self):
        return self.name


class LeadershipPage(Page):
    template = "people/leadership_page.html"
    parent_page_types = ["core.HomePage"]

    intro = models.TextField(blank=True, verbose_name="Вступление")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["leaders"] = Leader.objects.all()
        return context

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"
