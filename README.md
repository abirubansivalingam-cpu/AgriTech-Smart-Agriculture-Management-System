# AgriTech – Smart Agriculture Management System

A beginner-friendly Django web application for farmer profiles, farm records, crop planning, farm tasks, soil test history, and a farmer produce marketplace.

## Technology
- Python 3.11+ (recommended; compatible with current supported Django versions)
- Django 5.2
- SQLite by default; optional PostgreSQL
- HTML, CSS, JavaScript

## Features
1. Farmer registration, login and logout
2. Dashboard with farm/crop/task summary
3. Create and view multiple farms
4. Crop planning and status tracking
5. Farm task creation and completion
6. Soil pH and N-P-K test record history
7. Basic pH-based educational notes (not a substitute for agronomist advice)
8. Farmer produce listings and crop search
9. Django admin management
10. Automated tests and responsive interface

## Windows setup (PowerShell or CMD)
```bat
cd AgriTech_Smart_Agriculture_Complete_Project
py -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations core farms marketplace
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py test
python manage.py runserver
```
Open `http://127.0.0.1:8000/`. Do not append `/**` or tracking parameters. Admin: `http://127.0.0.1:8000/admin/`.

## Demo data
`python manage.py seed_demo` creates a demo farmer (`demo_farmer`, password `AgriDemo@123`) and sample farms/crops/tasks/soil records/listing if they do not already exist. Change the demo password before any public deployment.

## Optional PostgreSQL
Create a database named `agritech_db`. Set these environment variables before running migrations:
```bat
set DB_ENGINE=postgres
set DB_NAME=agritech_db
set DB_USER=postgres
set DB_PASSWORD=YOUR_POSTGRES_PASSWORD
set DB_HOST=127.0.0.1
set DB_PORT=5432
python manage.py migrate
```
Install `psycopg[binary]` from requirements. In PowerShell use `$env:DB_ENGINE="postgres"` etc.

## Main URL map
- `/` public home
- `/accounts/register/` registration
- `/accounts/login/` login
- `/dashboard/` farmer dashboard
- `/farms/` farm directory
- `/farms/new/` add farm
- `/farms/crops/new/` add crop
- `/farms/tasks/new/` add task
- `/farms/soil/new/` add soil test
- `/farms/recommendations/` soil insights
- `/marketplace/` produce listings
- `/marketplace/new/` publish produce
- `/admin/` admin site

## Notes and limitations
- Weather forecast and live external market prices are not connected; do not treat sample or manually entered data as live data.
- Crop guidance is intentionally basic and pH-oriented. Real crop, fertilizer and pesticide decisions require local soil reports and qualified agricultural advice.
- Add HTTPS, secure environment secrets, backups, privacy policy and production database settings before deployment.
