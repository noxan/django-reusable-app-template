# django-{{ app_name }}

Template for reusable django applications.

All following sections are just dummies and may not work as excepted.

## Key features

* Reusable template for new reusable django applications
* ...

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-{{ app_name }}

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-{{ app_name }}#egg=django-{{ app_name }}

Add `{{ app_name }}` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        '{{ app_name }}',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('{{ app_name }}.urls', namespace='{{ app_name }}')),
        ...
    )
