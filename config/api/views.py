from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Comment
from .serializer import CommentSerializer
from rest_framework import status

@api_view(['GET'])
def get_data(request: Request):
    cats = Comment.objects.all().order_by()
    serializer = CommentSerializer(cats, many=True)
    print(request.content_type)
    print(request.query_params)
    print(request.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_data(request: Request):
    serializer = CommentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_data(request: Request, id: int):
    category = get_object_or_404(Comment, id=id)
    serializer = CommentSerializer(instance=category, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_data(request: Request, id: int):
    category = get_object_or_404(Comment, id=id)
    category.delete()
    return Response(data={}, status=status.HTTP_204_NO_CONTENT)