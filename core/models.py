from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .blocks import (
    CardsBlock,
    DirectionsBlock,
    FeaturedNewsBlock,
    HeroBlock,
    IntroBlock,
    LatestNewsBlock,
    ValuesBlock,
)


class HomePage(Page):
    template = "core/home_page.html"
    max_count = 1
    subpage_types = [
        "core.OrganizationPage",
        "news.NewsIndexPage",
        "people.LeadershipPage",
        "awards.AwardsPage",
        "contacts.ContactsPage",
    ]

    content = StreamField(
        [
            ("hero", HeroBlock()),
            ("intro", IntroBlock()),
            ("cards", CardsBlock()),
            ("rich_text", blocks.RichTextBlock(label="Текстовый блок")),
            ("values", ValuesBlock()),
            ("directions", DirectionsBlock()),
            ("featured_news", FeaturedNewsBlock()),
            ("latest_news", LatestNewsBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Контент",
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"


class OrganizationPage(Page):
    template = "core/organization_page.html"
    parent_page_types = ["core.HomePage"]

    content = StreamField(
        [
            ("hero", HeroBlock()),
            ("intro", IntroBlock()),
            ("rich_text", blocks.RichTextBlock(label="Текстовый блок")),
            ("values", ValuesBlock()),
            ("directions", DirectionsBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Контент",
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Об организации"
        verbose_name_plural = "Об организации"
