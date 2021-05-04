from django.urls import path
from .views import CreatePhoneView,ListPhoneView,EditPhoneView,DeletePhoneView,IndexPhoneView,call_add,call_list,call_edit
from django_filters.views import FilterView
from .filters import PhoneFilter

app_name = 'phone'
urlpatterns = [
    path('',IndexPhoneView.as_view(),name='phone-index'),
    path('create',CreatePhoneView.as_view(),name='phone-create'),
    path('list',ListPhoneView.as_view(),name='phone-list'),
    path('edit/<int:pk>',EditPhoneView.as_view(),name='phone-edit'),
    path('delete/<int:pk>',DeletePhoneView.as_view(),name='phone-delete'),
    path('add-call/<int:pk>',call_add,name='phone-call-add'),
    path('show-call/<int:pk>',call_list,name='phone-call-show'),
    path('edit-call/<int:pk>',call_edit,name='phone-call-edit'),
    path('search/', FilterView.as_view(filterset_class=PhoneFilter,template_name='phone/search.html'), name='search'),
]