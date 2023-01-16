from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import CreateListViewSet


class CommentViewSet(viewsets.ModelViewSet):
    """Вью сет для работы с комментариями."""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(post=post, author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    """Вью сет для работы с постами"""
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вью сет для работы с группами"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    """Вью сет для работы с подписками"""
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('$following__username', )
    ordering = ('following__username', )

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
