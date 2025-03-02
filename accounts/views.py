from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import  UserSerializer,LoginSerializer
from .tokenauthentication import JWTAuthentication


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(status=405)

# @api_view(['POST'])
# def login_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         token = JWTAuthentication.generate_token(payload=serializer.data)
#         return Response({
#             "message": "User logged in successfully",
#             'token': token,
#             'user': serializer.data
#         }, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token = JWTAuthentication.generate_token({"id": user.id, "email": user.email})

            return Response({
                "message": "User logged in successfully",
                "token": token,
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=405)
