## Microtask-4

Set up the developer environment of SortingHat (muggle branch)

### Steps

1. Clone the project and checkout the muggle branch.
2. Added a virtual environment to the project. <code>mkdir venv && python -m venv venv && source venv/bin/activate</code>
3. Installed the django dependencies <code>pip install -r requirements.txt</code>
4. Installed some additional dependencies <code>pip install django-cors-headers wheel ) ( pip install mysqlclient==2.0.1 PyJWT==1.7.1</code>
5. Migrate model to database schema <code>./manage.py migrate --settings=config.settings.devel</code>
6. Create login credentials for /admin page <code>./manage.py createsuperuser --settings=config.settings.devel</code>
7. Run the server <code>./manage.py runserver --settings=config.settings.devel</code>

The above steps were about setting up the backend. The following steps are for setting up the frontend.

8. cd into <code>/ui</code>
9. Install dependencies <code>yarn install</code>
10. Start serving <code>yarn serve</code>

### Issues Faced

1. Ran into an issue about **sortinghat_db** not exisiting. Solved it by manually creating the table.
