from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import ContactsSerializer, BoardSerializer
from contacts.models import Contacts, Tasks
from rest_framework.decorators import api_view

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True) 
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def check_email(request):
    email = request.GET.get('email', None)
    if not email:
        return Response({"detail": "E-Mail ist erforderlich"}, status=status.HTTP_400_BAD_REQUEST)

    existing_contact = Contacts.objects.filter(email=email).exists()
    if existing_contact:
        return Response({"doesExist": True}, status=status.HTTP_200_OK)
    return Response({"doesExist": False}, status=status.HTTP_200_OK)   
    
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = BoardSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True) 
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)