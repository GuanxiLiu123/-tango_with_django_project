import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()

from rango.models import Category, Page

def populate():
    categories = {
        "Python": {
            "views": 128,
            "likes": 64,
            "pages": [
                {"title": "Official Python Tutorial", "url": "http://docs.python.org/3/tutorial/"},
                {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/"},
                {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/"}
            ]
        },
        "Django": {
            "views": 64,
            "likes": 32,
            "pages": [
                {"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/2.1/intro/tutorial01/"},
                {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
                {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"}
            ]
        },
        "Other Frameworks": {
            "views": 32,
            "likes": 16,
            "pages": [
                {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/"},
                {"title": "Flask", "url": "http://flask.pocoo.org"}
            ]
        }
    }

    for cat_name, cat_data in categories.items():
        cat = add_category(cat_name, cat_data["views"], cat_data["likes"])
        for page in cat_data["pages"]:
            add_page(cat, page["title"], page["url"])

    # Print populated data
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c.name}: {p.title}')

def add_page(category, title, url, views=0):
    p, created = Page.objects.get_or_create(category=category, title=title)
    p.url = url
    p.views = views
    p.save()
    return p

def add_category(name, views=0, likes=0):
    c, created = Category.objects.get_or_create(name=name)
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
