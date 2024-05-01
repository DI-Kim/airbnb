from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from .serializers import PrivateUserSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_user = serializer.save()
            serializer = PrivateUserSerializer(updated_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError

        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            # password를 set_password() 메소드에 넣으면 해시화(절대로 raw password를 저장하지 말자.)
            updated_user.set_password(password)
            # 비밀번호가 업데이트된 유저 db에 저장
            updated_user.save()
            serializer = PrivateUserSerializer(updated_user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
