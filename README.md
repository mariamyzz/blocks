# blocks

*Blocks* is the Wagtail/Django application can helps you 
to make a website page from predisigned blocks.

Settings
---------------
First of all you will need to rename file ``/congif/.env.template`` to ``/congif/.env``
Next step is open ``/congif/.env`` and replace __CHANGEME__ in ``DJANGO_SECRET_KEY=__CHANGEME__`` to your secret key

Installation
------------
You will need
- ``pip install pipenv``
- ``pipenv install``
- ``pipenv run python manage.py migrate``
- ``pipenv run python manage.py createsuperuser``

Run
---
- ``pipenv run python manage.py runserver``