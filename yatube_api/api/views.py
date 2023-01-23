from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    """Вью сет для работы с комментариями."""
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), author=self.request.user)


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
