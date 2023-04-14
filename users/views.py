from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .permissions import IfEmployeeReadAllOrReadSelf
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewSpecif(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IfEmployeeReadAllOrReadSelf]

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(
            instance=user,
            data=req.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status.HTTP_200_OK)
