find /app/backend -path '*/migrations/*.py' -not -name '__init__.py' -delete 
find /app/backend -path '*/migrations/*.pyc' -delete 
 
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
