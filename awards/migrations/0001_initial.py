from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160, verbose_name="Название")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.SET_NULL,
                        related_name="awards",
                        to="wagtailimages.image",
                        verbose_name="Изображение",
                    ),
                ),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="Сортировка")),
            ],
            options={
                "verbose_name": "Награда",
                "verbose_name_plural": "Награды",
                "ordering": ["sort_order", "title"],
            },
        ),
        migrations.CreateModel(
            name="AwardsPage",
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
                "verbose_name": "Оценка деятельности",
                "verbose_name_plural": "Оценка деятельности",
            },
            bases=("wagtailcore.page",),
        ),
    ]
