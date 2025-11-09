from rest_framework import serializers
from contacts.models import Contacts, Tasks, Subtask
from datetime import date
from django.contrib.auth.models import User
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
    
        
class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, allow_blank=False)
    due_date = serializers.DateField(required=True)
    assigned_to = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Contacts.objects.all()
    )
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

    def validate_assigned_to(self, value):
        user = self.context['request'].user
        if user.is_anonymous:
            user = User.objects.first()  # Dummy-User für Entwicklung
        allowed_contacts = Contacts.objects.filter(user=user)
        for contact in value:
            if contact not in allowed_contacts:
                raise serializers.ValidationError("Ungültiger Kontakt ausgewählt.")
        return value

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'description', 'done']