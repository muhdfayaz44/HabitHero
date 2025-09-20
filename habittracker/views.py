from rest_framework import viewsets
from .models import Category, Habit, CheckIn
from .serializers import CategorySerializer, HabitSerializer ,CheckInSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer