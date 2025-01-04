from rest_framework import serializers
from contacts.models import Contacts, Tasks, Subtask

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'title',
            'description',
            'due_date',
            'board',
            'priority',
            'subtasks',
            'category',
            'assigned_to',
        ]

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'description', 'done']