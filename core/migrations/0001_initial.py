from django.db import migrations, models
import wagtail.blocks
import wagtail.fields

import core.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            ("hero", core.blocks.HeroBlock()),
                            ("intro", core.blocks.IntroBlock()),
                            ("cards", core.blocks.CardsBlock()),
                            ("rich_text", wagtail.blocks.RichTextBlock(label="Текстовый блок")),
                            ("values", core.blocks.ValuesBlock()),
                            ("directions", core.blocks.DirectionsBlock()),
                            ("featured_news", core.blocks.FeaturedNewsBlock()),
                            ("latest_news", core.blocks.LatestNewsBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Контент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Главная",
                "verbose_name_plural": "Главная",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="OrganizationPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            ("hero", core.blocks.HeroBlock()),
                            ("intro", core.blocks.IntroBlock()),
                            ("rich_text", wagtail.blocks.RichTextBlock(label="Текстовый блок")),
                            ("values", core.blocks.ValuesBlock()),
                            ("directions", core.blocks.DirectionsBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Контент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Об организации",
                "verbose_name_plural": "Об организации",
            },
            bases=("wagtailcore.page",),
        ),
    ]
