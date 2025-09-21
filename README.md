# Habit Hero - Backend

Django + DRF API for Habit Hero.

## Quick setup (backend)
1. Clone repo:
   git clone https://github.com/YOUR_USERNAME/YOUR_BACKEND_REPO.git
2. Create venv & install:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
3. Migrate & run:
   python manage.py migrate
   python manage.py createsuperuser  (optional)
   python manage.py runserver

## API endpoints
- /api/categories/  (GET, POST)
- /api/habits/      (GET, POST)
- /api/checkins/    (GET, POST)
- /api/habits/{id}/analytics/ (GET)

## Demo
Demo video: "C:\Users\muham\Videos\Screen Recordings\Screen Recording 2025-09-21 222234.mp4"
