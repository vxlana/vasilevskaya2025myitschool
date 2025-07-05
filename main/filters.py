import django_filters
from .models import ClothingItem, Size, Category

class ClothingItemFilter(django_filters.FilterSet):
    size = django_filters.ModelMultipleChoiceFilter(
        field_name='sizes',
        queryset=Size.objects.all(),
        conjoined=True
    )
    category = django_filters.ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория'
    )
    price_min = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Мин. цена'
    )
    price_max = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Макс. цена'
    )
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Название')

    class Meta:
        model = ClothingItem
        fields = ['size', 'category', 'price_min', 'price_max', 'name']