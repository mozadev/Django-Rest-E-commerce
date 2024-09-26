from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):

    #list
    if request.method == 'GET':
        #queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)

        # test_data = {
        #     'name': 'jose',
        #     'email': 'test@gmail.com'
        # }
        # test_user = TestUserSerializer(data = test_data, context = test_data)
        # if test_user.is_valid():
        #     user_instance = test_user.save()
        #     print(user_instance)
        # else:
        #     print(test_user.errors)
        
        return Response(users_serializer.data, status=status.HTTP_200_OK   )
    
    #create
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        
        #validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User created!'}, status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    #queryset
    user = User.objects.filter(id = pk).first()

    #validation
    if user: 

        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            user_serializer = TestUserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'User deleted!'}, status=status.HTTP_200_OK)
    
    return Response({'message': 'User not found!'}, status=status.HTTP_400_BAD_REQUEST)
  





















# class UserAPIView(APIView):

#     def get(self, request):
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many = True)
#         return Response(users_serializer.data)
    
    
    
