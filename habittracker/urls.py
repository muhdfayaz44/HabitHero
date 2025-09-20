from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, HabitViewSet, CheckInViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'checkins', CheckInViewSet)

urlpatterns = [
    path('',include(router.urls)),
]