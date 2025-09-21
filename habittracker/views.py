from rest_framework import viewsets
from .models import Category, Habit, CheckIn
from .serializers import CategorySerializer, HabitSerializer ,CheckInSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, timedelta
from collections import Counter
from .models import Habit, CheckIn
from django.http import JsonResponse


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

@api_view(['GET'])
def habit_analytics(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    checkins = habit.checkins.all()

    # Total expected check-ins
    total_days = (date.today() - habit.start_date).days + 1
    if habit.frequency == 'weekly':
        total_expected = total_days // 7 + (1 if total_days % 7 else 0)
    else:
        total_expected = total_days

    completed_checkins = checkins.filter(status=True).count()
    success_rate = round((completed_checkins / total_expected) * 100, 2) if total_expected > 0 else 0

    # Streak
    streak = 0
    current_date = date.today()
    while checkins.filter(date=current_date, status=True).exists():
        streak += 1
        current_date -= timedelta(days=1 if habit.frequency == 'daily' else 7)

    # ✅ Count check-ins by weekday
    completed_dates = checkins.filter(status=True).values_list('date', flat=True)
    day_counts = Counter(d.weekday() for d in completed_dates)  # 0=Mon
    best_day = max(day_counts, key=day_counts.get) if day_counts else None

    # Make a dict with 0–6 weekdays
    weekly_distribution = {i: day_counts.get(i, 0) for i in range(7)}

    return JsonResponse({
        "habit": habit.name,
        "success_rate": success_rate,
        "streak": streak,
        "best_day": best_day,
        "completed_checkins": completed_checkins,
        "total_expected": total_expected,
        "weekly_distribution": weekly_distribution
    })