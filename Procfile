web: python manage.py runserver
web: gunicorn whoyouproject.wsgi --log-file -
heroku ps:scale web=1