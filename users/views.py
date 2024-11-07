from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework import status

import jwt, datetime

# Create your views here.
class Register(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'message':'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({'status':'error', 'message':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user=models.User.objects.filter(email=email).first()
        if user is None:
            return Response({'status':'error', 'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
            return Response({'status':'error', 'message':'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        payload={
            'id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret_key', algorithm='HS256')
        
        response=Response()
        response.set_cookie(key='token', value=token,httponly=True)
        response.data={
            'message':'login successful',
            'token':token,
        }
        return response
    
    
class UserView(APIView):
    def get(self, request):
        token=request.COOKIES.get('token')
        if not token:
            return Response({'status':'error', 'message':'Unauthenticated!'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
         payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'status':'error', 'message':'Unauthenticated!'}, status=status.HTTP_401_UNAUTHORIZED)
        
        user=models.User.objects.filter(id=payload['id']).first()
        serializer=serializers.UserSerializer(user)
        return Response(serializer.data)
    
    
class LogOutView(APIView):
    def post(self, request):
        response=Response()
        response.delete_cookie('token')
        response.data={'message':'logout successful'}
        return response