from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    subtitle = blocks.TextBlock(label="Подзаголовок", required=False)
    image = ImageChooserBlock(label="Изображение", required=False)
    cta_text = blocks.CharBlock(label="Текст кнопки", required=False)
    cta_page = blocks.PageChooserBlock(label="Страница кнопки", required=False)

    class Meta:
        icon = "image"
        label = "Hero"
        template = "blocks/hero_block.html"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.TextBlock(label="Текст", required=False)
    image = ImageChooserBlock(label="Изображение", required=False)

    class Meta:
        icon = "doc-full"
        label = "Карточка"
        template = "blocks/card_block.html"


class IntroBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.TextBlock(label="Текст")
    cta_text = blocks.CharBlock(label="Текст кнопки", required=False)
    cta_page = blocks.PageChooserBlock(label="Страница кнопки", required=False)

    class Meta:
        icon = "placeholder"
        label = "Интро с кнопкой"
        template = "blocks/intro_block.html"


class CardsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    cards = blocks.ListBlock(CardBlock(), label="Карточки", min_num=1)

    class Meta:
        icon = "list-ul"
        label = "Карточки/обложки"
        template = "blocks/cards_block.html"


class ValueItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Ценность")
    description = blocks.TextBlock(label="Описание")

    class Meta:
        icon = "tick"
        label = "Ценность"
        template = "blocks/value_item_block.html"


class ValuesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    items = blocks.ListBlock(ValueItemBlock(), label="Список ценностей", min_num=1)

    class Meta:
        icon = "form"
        label = "Список ценностей"
        template = "blocks/values_block.html"


class DirectionsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    items = blocks.ListBlock(blocks.CharBlock(label="Направление"), label="Направления", min_num=1)

    class Meta:
        icon = "site"
        label = "Направления деятельности"
        template = "blocks/directions_block.html"


class FeaturedNewsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    pages = blocks.ListBlock(
        blocks.PageChooserBlock(page_type=["news.NewsPage"]),
        label="Выбранные новости",
        min_num=1,
    )

    class Meta:
        icon = "doc-full-inverse"
        label = "Выбранные новости"
        template = "blocks/featured_news_block.html"


class LatestNewsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    count = blocks.IntegerBlock(label="Количество", default=3, min_value=1, max_value=9)

    class Meta:
        icon = "date"
        label = "Последние новости"
        template = "blocks/latest_news_block.html"
