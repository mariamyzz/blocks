# blocks

*Blocks* is the Wagtail/Django application can helps you 
to make a website page from predisigned blocks.

We are using
- ``python3.6``
- ``yarn``
- ``gulp``

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
- ``brew install yarn`` only for mac [Another platforms](https://yarnpkg.com/lang/en/docs/install/#mac-tab)
- ``yarn install``

Run
---
- ``bash start`` or commands below
- ``pipenv run python manage.py runserver``
- ``gulp``