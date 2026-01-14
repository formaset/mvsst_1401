from pathlib import Path

from django.contrib.auth.models import Group, Permission
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone
from wagtail.images.models import Image
from wagtail.models import Page, Site, GroupPagePermission

from awards.models import Award, AwardsPage
from contacts.models import ContactsPage
from core.models import HomePage, OrganizationPage
from news.models import NewsIndexPage, NewsPage
from people.models import Leader, LeadershipPage


MISSION_TEXT = (
    "Создавать комфортную и безопасную городскую среду, объединяя традиции "
    "столичного строительства с современными технологиями благоустройства для "
    "миллионов жителей Москвы."
)

COMPANY_TEXT = (
    "Организация основана 1 октября 2024 года, учредитель — ГУП «Мосводосток». "
    "Деятельность охватывает благоустройство улиц и сезонной инфраструктуры, "
    "капитальный ремонт многоквартирных домов и объектов образования, "
    "строительство производственных баз и выполнение специализированных задач "
    "учредителя. В штате — около 4000 работников."
)

VALUES = [
    {
        "title": "Качество",
        "description": "Строим на совесть и соблюдаем стандарты, отвечая за результат своим именем.",
    },
    {
        "title": "Сроки",
        "description": "Ценим ритм мегаполиса и работаем без простоев и срывов графика.",
    },
    {
        "title": "Безопасность",
        "description": "Жизнь людей — безусловный приоритет и основа нашей культуры труда.",
    },
    {
        "title": "Команда",
        "description": "Мы — единый механизм, основанный на уважении и взаимопомощи.",
    },
]

DIRECTIONS = [
    "Благоустройство улиц и общественных пространств",
    "Сезонная городская инфраструктура",
    "Капитальный ремонт МКД и объектов образования",
    "Строительство производственных баз",
    "Выполнение спецзадач учредителя",
]


class Command(BaseCommand):
    help = "Создаёт стартовые страницы и контент для сайта."

    def handle(self, *args, **options):
        root = Page.get_first_root_node()
        home = HomePage.objects.first()
        if not home:
            home = HomePage(title="Главная", slug="home")
            root.add_child(instance=home)
            home.save_revision().publish()

        if not home.get_children().filter(slug="organization").exists():
            org_page = OrganizationPage(title="Об организации", slug="organization")
            home.add_child(instance=org_page)
            org_page.content = self._build_org_content()
            org_page.save_revision().publish()
        else:
            org_page = home.get_children().get(slug="organization").specific

        if not home.content:
            home.content = self._build_home_content(org_page)
            home.save_revision().publish()

        if not home.get_children().filter(slug="leadership").exists():
            leadership = LeadershipPage(title="Руководство", slug="leadership")
            home.add_child(instance=leadership)
            leadership.save_revision().publish()

        if not home.get_children().filter(slug="assessment").exists():
            assessment = AwardsPage(title="Оценка деятельности организации", slug="assessment")
            home.add_child(instance=assessment)
            assessment.save_revision().publish()

        if not home.get_children().filter(slug="news").exists():
            news_index = NewsIndexPage(title="Новости", slug="news")
            home.add_child(instance=news_index)
            news_index.save_revision().publish()
        else:
            news_index = home.get_children().get(slug="news").specific

        if not home.get_children().filter(slug="contacts").exists():
            contacts = ContactsPage(
                title="Контакты",
                slug="contacts",
                phone="+7 (495) 000-00-00",
                email="info@mvsst.ru",
                legal_address="г. Москва, ул. Примерная, д. 1",
                actual_address="г. Москва, ул. Примерная, д. 1",
                full_name="Автономная некоммерческая организация по развитию городской среды «МосводостокСтройТрест»",
                short_name="АНО «МосводостокСтройТрест»",
            )
            home.add_child(instance=contacts)
            contacts.save_revision().publish()

        if not news_index.get_children().exists():
            cover = self._create_placeholder_image("news-cover.jpg")
            news_page = NewsPage(
                title="Новая команда начала сезон благоустройства",
                intro="Сезонные работы стартовали с обновления ключевых городских маршрутов.",
                date=timezone.now().date(),
                cover_image=cover,
                body=self._build_news_body(),
            )
            news_index.add_child(instance=news_page)
            news_page.save_revision().publish()

        if not Leader.objects.exists():
            leader_photo = self._create_placeholder_image("leader.jpg")
            Leader.objects.create(
                name="Ирина Петрова",
                title="Генеральный директор",
                photo=leader_photo,
                sort_order=1,
            )

        if not Award.objects.exists():
            award_image = self._create_placeholder_image("award.jpg")
            Award.objects.create(
                title="Благодарность за благоустройство",
                description="Награда за вклад в развитие городской инфраструктуры.",
                image=award_image,
                sort_order=1,
            )

        self._ensure_site(home)
        self._ensure_news_editor_permissions(news_index)
        self.stdout.write(self.style.SUCCESS("Bootstrap завершён"))

    def _create_placeholder_image(self, filename):
        media_root = Path("media")
        media_root.mkdir(exist_ok=True)
        file_path = media_root / filename
        if not file_path.exists():
            try:
                from PIL import Image as PilImage, ImageDraw

                image = PilImage.new("RGB", (1200, 800), color=(155, 203, 235))
                draw = ImageDraw.Draw(image)
                draw.rectangle([(60, 60), (1140, 740)], outline=(0, 47, 108), width=8)
                draw.text((120, 120), "АНО МосводостокСтройТрест", fill=(0, 47, 108))
                image.save(file_path)
            except Exception:
                file_path.write_bytes(b"")
        image = Image.objects.filter(title=filename).first()
        if image:
            return image
        with file_path.open("rb") as file_handle:
            image = Image(title=filename, file=File(file_handle))
            image.save()
        return image

    def _build_org_content(self):
        return [
            (
                "hero",
                {
                    "title": "Об организации",
                    "subtitle": COMPANY_TEXT,
                },
            ),
            (
                "rich_text",
                f"<h2>Миссия</h2><p>{MISSION_TEXT}</p>",
            ),
            (
                "values",
                {
                    "heading": "Ценности",
                    "items": VALUES,
                },
            ),
            (
                "directions",
                {
                    "heading": "Направления деятельности",
                    "items": DIRECTIONS,
                },
            ),
        ]

    def _build_home_content(self, organization_page=None):
        return [
            (
                "hero",
                {
                    "title": "Развиваем городскую среду Москвы",
                    "subtitle": "АНО «МосводостокСтройТрест» объединяет лучшие практики строительства и благоустройства.",
                    "cta_text": "Об организации",
                    "cta_page": organization_page,
                },
            ),
            (
                "cards",
                {
                    "heading": "Ключевые направления",
                    "cards": [
                        {"title": "Благоустройство улиц", "text": "Проектируем и обновляем городские пространства."},
                        {"title": "Сезонная инфраструктура", "text": "Поддерживаем комфорт жителей круглый год."},
                        {"title": "Капремонт МКД", "text": "Обновляем жилые и социальные объекты."},
                    ],
                },
            ),
            (
                "intro",
                {
                    "title": "Об организации",
                    "text": "Мы создаём комфортную среду, сочетая опыт столичного строительства и современные решения.",
                    "cta_text": "Подробнее",
                    "cta_page": organization_page,
                },
            ),
            (
                "latest_news",
                {"heading": "Последние новости", "count": 3},
            ),
        ]

    def _build_news_body(self):
        return [
            ("paragraph", "<p>Городские службы приступили к сезонным работам на ключевых участках.</p>"),
            ("heading", "Ключевые цифры"),
            ("key_number", {"number": "48", "label": "команд на линии"}),
            ("callout", {"title": "Важно", "text": "Все работы выполняются с усиленными мерами безопасности."}),
            ("divider", {}),
            ("quote", {"text": "Мы работаем для жителей, сохраняя темп города.", "author": "Пресс-служба"}),
        ]

    def _ensure_site(self, home):
        if not Site.objects.filter(is_default_site=True).exists():
            Site.objects.create(hostname="localhost", root_page=home, is_default_site=True)

    def _ensure_news_editor_permissions(self, news_index):
        group, _ = Group.objects.get_or_create(name="Редактор новостей")
        permissions = Permission.objects.filter(
            codename__in=[
                "access_admin",
                "add_newspage",
                "change_newspage",
                "add_image",
                "change_image",
                "add_document",
                "change_document",
            ]
        )
        group.permissions.set(permissions)
        GroupPagePermission.objects.get_or_create(
            group=group,
            page=news_index,
            permission_type="add",
        )
        GroupPagePermission.objects.get_or_create(
            group=group,
            page=news_index,
            permission_type="edit",
        )
        GroupPagePermission.objects.get_or_create(
            group=group,
            page=news_index,
            permission_type="publish",
        )
