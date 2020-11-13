from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# class UserAuthentication(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context=('request':request))
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validation_data['user']
#         token.created=Token.objects.get_or_create(user=user)
#         return Response(Token.Key)

class UserList(APIView):
    def get(self, request):
        model = Users.objects.all()
        serializers = UsersSerializers(model, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers=UsersSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    
    def get(self, request, id):
        try:
            model = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response (f"User with {id} is not found in database", status=status.HTTP_404_NOT_FOUND)
        serializers = UsersSerializers(model)
        return Response(serializers.data)

    def put(self, request, id):
        try:
            model = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response (f"User with {id} is not found in database", status=status.HTTP_404_NOT_FOUND)
        serializers=UsersSerializers(model, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            model = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response (f"User with {id} is not found in database", status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
