import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def markdownify(text):
    if not text:
        return ""

    html = markdown.markdown(
        text,
        extensions=[
            "extra",
            "fenced_code",
            "tables",
            "sane_lists",
        ],
    )

    return mark_safe(html)