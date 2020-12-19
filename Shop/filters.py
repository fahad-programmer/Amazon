from Shop.models import Product
import django_filters


class ProductFilter(django_filters.FilterSet):

    price__gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lt')

    rating__lt = django_filters.NumberFilter(
        field_name='rating', lookup_expr='gt')

    brand = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = []
