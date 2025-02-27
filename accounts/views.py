from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  UserSerializer

def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(status=405)
# Create your views here.
