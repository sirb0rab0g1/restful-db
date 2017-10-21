web: python manage.py runserver
web: python manage.py collectstatic
web: gunicorn resttutorial.wsgi --log-file -
heroku ps:scale web=1