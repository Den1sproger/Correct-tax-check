run:
	cd correct_tax && python3 manage.py runserver
createmigr:
	cd correct_tax && python3 manage.py makemigrations
migrate:
	cd correct_tax && python3 manage.py migrate
static:
	cd correct_tax && python3 manage.py collectstatic --no-input