from wagtail.models import Page, Site


NAV_SLUGS = {
    "organization": "organization",
    "leadership": "leadership",
    "assessment": "assessment",
    "news": "news",
    "contacts": "contacts",
}


def navigation(request):
    site = Site.find_for_request(request)
    root = site.root_page if site else None
    pages = {}
    if root:
        for key, slug in NAV_SLUGS.items():
            page = root.get_children().live().filter(slug=slug).first()
            if page:
                pages[key] = page.specific
    return {
        "nav_pages": pages,
    }
