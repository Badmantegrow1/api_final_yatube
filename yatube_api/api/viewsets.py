from rest_framework import mixins, viewsets


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Собираем свой вьюсет для подписок. Создание и вывод списком."""
    pass
