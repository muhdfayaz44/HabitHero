from rest_framework import serializers
from .models import Category, Habit, CheckIn

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

class CheckInSerializer(serializers.ModelSerializer):
    habit_name = serializers.CharField(source='habit.name', read_only=True)
    

    class Meta:
        model = CheckIn
        fields = ['id', 'habit', 'habit_name', 'date', 'status']
