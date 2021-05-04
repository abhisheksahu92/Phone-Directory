from phone.models import PhoneModel
import django_filters

class PhoneFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.NumberFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PhoneModel
        fields = ['first_name', 'last_name','phone','email']
