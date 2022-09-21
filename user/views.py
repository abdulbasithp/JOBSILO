from rest_framework.viewsets import ViewSet
from .models import Account
from .serializers import SignUpSerializer, UserViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .token import create_jwt_pair_tokens
from seeker.models import SeekerProfile
from recruiter.models import RecruiterProfile


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request):
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)
        role = request.data.get('role')
        email = request.data.get('email')
        
        if serializer.is_valid():
            serializer.save()
            if role == 'seeker':
                user = Account.objects.get(email=email)
                SeekerProfile.objects.create(seeker=user)
            elif role == 'recruiter':
                user = Account.objects.get(email=email)
                RecruiterProfile.objects.create(recruiter=user)
            else:
                print('user role supplied is not seeker of recruiter but base user created!')
            response = {
                'message': "User Created Successfully",
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request:Request):
        """using email and password post request will return response tokens for authentication:
                request :   email & password,response :  access & refresh"""
        email = request.data.get('email')
        password = request.data.get('password') 
        user = authenticate(request, email=email, password=password)

        if user is not None:        
            tokens = create_jwt_pair_tokens(user) 
            profile = {}                                                                                                                                                                                                                                                                                                                                          
            if user.role == 'seeker':
                profile = SeekerProfile.objects.get(seeker=user)
            elif user.role == 'recruiter':
                profile = RecruiterProfile.objects.get(recruiter=user)
            response = {
                "message": "Login successfull",
                "token": tokens,
                "user" : {
                    "user_id":user.id,
                    "email":user.email,
                    "role":user.role,
                    'profile_id':profile.id
                }
            } 
            
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={
                "message": "Invalid email or password!"
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        content = {
            "user": str(request.user)
        }
        return Response(content, status=status.HTTP_200_OK)


class UserView(generics.RetrieveAPIView):
    """user details only [email, firstname, middlename, lastname, phone number, city , dob, profile image ]"""
    permission_classes = []
    serializer_class = UserViewSerializer
    queryset = Account.objects.all()



    
# b1 branch created


