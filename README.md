# Habit Hero - Backend

Django + DRF API for Habit Hero.

# Tech Stack
-Backend: Django, Django REST Framework
-API Requests: Axios (frontend)
-CORS Handling: django-cors-headers
-Database: SQLite

## Quick setup (backend)
1. Clone repo:
   git clone https://github.com/muhdfayaz44/HabitHero.git
2. Create venv & install:
   python -m venv env
   env\Scripts\activate
3. Migrate & run:
   python manage.py migrate
   python manage.py createsuperuser 
   python manage.py runserver

## API endpoints
- /api/categories/  (GET, POST)
- /api/habits/      (GET, POST)
- /api/checkins/    (GET, POST)
- /api/habits/{id}/analytics/ (GET)

