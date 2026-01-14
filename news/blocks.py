from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Изображение")
    caption = blocks.CharBlock(label="Подпись", required=False)

    class Meta:
        icon = "image"
        label = "Изображение"
        template = "news/blocks/image_block.html"


class VideoBlock(blocks.StructBlock):
    video = DocumentChooserBlock(label="Видео файл")
    caption = blocks.CharBlock(label="Подпись", required=False)

    class Meta:
        icon = "media"
        label = "Видео"
        template = "news/blocks/video_block.html"


class QuoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Цитата")
    author = blocks.CharBlock(label="Источник", required=False)

    class Meta:
        icon = "openquote"
        label = "Цитата"
        template = "news/blocks/quote_block.html"


class CalloutBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок", required=False)
    text = blocks.TextBlock(label="Текст")

    class Meta:
        icon = "placeholder"
        label = "Выделение"
        template = "news/blocks/callout_block.html"


class DividerBlock(blocks.StructBlock):
    class Meta:
        icon = "horizontalrule"
        label = "Разделитель"
        template = "news/blocks/divider_block.html"


class KeyNumberBlock(blocks.StructBlock):
    number = blocks.CharBlock(label="Число")
    label = blocks.CharBlock(label="Подпись")

    class Meta:
        icon = "form"
        label = "Ключевая цифра"
        template = "news/blocks/key_number_block.html"


class GalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(label="Изображение"), min_num=2)

    class Meta:
        icon = "image"
        label = "Галерея"
        template = "news/blocks/gallery_block.html"
