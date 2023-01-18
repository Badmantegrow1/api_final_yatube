from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки подписок."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def validate_following(self, following):
        follower = self.context['request'].user
        if following == self.context['request'].user:
            raise ValidationError("Подписка на самого себя не предусмотрена.")

        entry = Follow.objects.filter(user=follower, following=following)
        if entry.exists():
            raise ValidationError(f"Подписка на {following} уже оформлена!")

        return following


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', )


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки постов."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для упаковки групп."""
    class Meta:
        model = Group
        fields = '__all__'
