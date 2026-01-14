from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leader",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="ФИО")),
                ("title", models.CharField(max_length=120, verbose_name="Должность")),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.SET_NULL,
                        related_name="leaders",
                        to="wagtailimages.image",
                        verbose_name="Фото",
                    ),
                ),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="Сортировка")),
            ],
            options={
                "verbose_name": "Руководитель",
                "verbose_name_plural": "Руководство",
                "ordering": ["sort_order", "name"],
            },
        ),
        migrations.CreateModel(
            name="LeadershipPage",
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
                "verbose_name": "Руководство",
                "verbose_name_plural": "Руководство",
            },
            bases=("wagtailcore.page",),
        ),
    ]
