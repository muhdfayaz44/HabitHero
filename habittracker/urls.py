from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, HabitViewSet, CheckInViewSet
from django.urls import path, include
from .views import CategoryViewSet, HabitViewSet, CheckInViewSet, habit_analytics

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'checkins', CheckInViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('habits/<int:habit_id>/analytics/', habit_analytics, name='habit-analytics'),
]