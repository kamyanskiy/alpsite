from mezzanine import template
from django.contrib.auth import get_user_model
from mezzanine.pages.models import Page

User = get_user_model()

register = template.Library()


@register.as_tag
def docpage_recent_articles(limit=5, username=None):
    """
    Put a list of recently published docpage articles into the template
    context.

    Usage::

        {% docpage_recent_articles 5 as articles %}
        {% docpage_recent_articles 5 username=admin as articles %}

    """
    doc_pages = Page.objects.published()
    if username is not None:
        try:
            author = User.objects.get(username=username)
            doc_pages = doc_pages.filter(user=author)
        except User.DoesNotExist:
            return []
    return list(doc_pages[:limit])