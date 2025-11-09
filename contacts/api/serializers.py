from rest_framework import serializers
from contacts.models import Contacts, Tasks, Subtask
from datetime import date

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
    
        
class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, allow_blank=False)
    due_date = serializers.DateField(required=True)
    class Meta:
        model = Tasks
        fields = '__all__'
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title darf nicht leer sein.")
        return value
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Das Fälligkeitsdatum darf nicht in der Vergangenheit liegen.")
        return value

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'description', 'done']