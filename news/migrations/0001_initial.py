from django.db import migrations, models
from django.utils import timezone
import wagtail.blocks
import wagtail.fields

import news.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsIndexPage",
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
                ("intro", models.TextField(blank=True, verbose_name="Вступление")),
            ],
            options={
                "verbose_name": "Новости",
                "verbose_name_plural": "Новости",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsPage",
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
                ("date", models.DateField(default=timezone.now, verbose_name="Дата публикации")),
                ("intro", models.CharField(max_length=255, verbose_name="Краткий лид")),
                (
                    "cover_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.SET_NULL,
                        related_name="news_cover",
                        to="wagtailimages.image",
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("paragraph", wagtail.blocks.RichTextBlock(label="Абзац")),
                            ("heading", wagtail.blocks.CharBlock(label="Заголовок")),
                            ("image", news.blocks.ImageBlock()),
                            ("video", news.blocks.VideoBlock()),
                            ("quote", news.blocks.QuoteBlock()),
                            ("callout", news.blocks.CalloutBlock()),
                            ("divider", news.blocks.DividerBlock()),
                            ("key_number", news.blocks.KeyNumberBlock()),
                            ("gallery", news.blocks.GalleryBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Контент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
            bases=("wagtailcore.page",),
        ),
    ]
