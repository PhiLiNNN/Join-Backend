from rest_framework import serializers
from contacts.models import Contacts, Tasks

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
        
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
           