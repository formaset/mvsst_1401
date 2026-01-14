from django import template
from news.models import NewsPage

register = template.Library()


@register.simple_tag
def latest_news(count=3):
    return NewsPage.objects.live().order_by("-date")[:count]
