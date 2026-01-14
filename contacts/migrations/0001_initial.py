from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactsPage",
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
                ("phone", models.CharField(max_length=40, verbose_name="Телефон")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("legal_address", models.CharField(max_length=255, verbose_name="Юридический адрес")),
                ("actual_address", models.CharField(max_length=255, verbose_name="Фактический адрес")),
                (
                    "working_hours",
                    models.CharField(
                        default="ПН–ЧТ 08:00–17:00, ПТ 08:00–16:00, перерыв 12:00–13:00",
                        max_length=255,
                        verbose_name="График работы",
                    ),
                ),
                ("full_name", models.CharField(max_length=255, verbose_name="Полное наименование")),
                ("short_name", models.CharField(max_length=255, verbose_name="Сокращённое наименование")),
                (
                    "map_embed",
                    models.TextField(
                        blank=True,
                        help_text="Вставьте ссылку или iframe-код. Разрешены домены yandex.*",
                        verbose_name="Yandex Maps embed URL / iframe code",
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
            },
            bases=("wagtailcore.page",),
        ),
    ]
