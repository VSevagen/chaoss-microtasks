## Microtask-4

Set up the developer environment of SortingHat (muggle branch)

### Steps

1. Clone the project and checkout the muggle branch.
2. Added a virtual environment to the project. ( mkdir venv && python -m venv venv && source venv/bin/activate )
3. Installed the django dependencies ( pip install -r requirements.txt )
4. Installed some additional dependencies ( pip install django-cors-headers wheel ) ( pip install mysqlclient==2.0.1 PyJWT==1.7.1 )
5. Migrate model to database schema ( ./manage.py migrate --settings=config.settings.devel )
6. Create login credentials for /admin page ( ./manage.py createsuperuser --settings=config.settings.devel )
7. Run the server ( ./manage.py runserver --settings=config.settings.devel )

The above steps were about setting up the backend. The following steps are for setting up the frontend.

8. cd into /ui
9. Install dependencies (yarn install)
10. Start serving ( yarn serve )

### Issues Faced

1. Ran into an issue about **sortinghat_db** not exisiting. Solved it by manually creating the table.

Here is a small demo
