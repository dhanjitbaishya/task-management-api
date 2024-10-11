from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value
