from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Award(models.Model):
    title = models.CharField(max_length=160, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="awards",
        verbose_name="Изображение",
    )
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Сортировка")

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order", "title"]
        verbose_name = "Награда"
        verbose_name_plural = "Награды"

    def __str__(self):
        return self.title


class AwardsPage(Page):
    template = "awards/awards_page.html"
    parent_page_types = ["core.HomePage"]

    intro = models.TextField(blank=True, verbose_name="Вступление")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["awards"] = Award.objects.all()
        return context

    class Meta:
        verbose_name = "Оценка деятельности"
        verbose_name_plural = "Оценка деятельности"
