from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PhoneModel,CallHistoryModel
from .forms import PhoneForm,PhoneUpdateForm,CallForm

class IndexPhoneView(TemplateView):
    template_name = 'phone/index.html'

class CreatePhoneView(CreateView):
    form_class = PhoneForm
    model = PhoneModel
    template_name = 'phone/create.html'
    error_css_class = 'error'
    success_url = reverse_lazy('phone:phone-list')

class ListPhoneView(ListView):
    model = PhoneModel
    template_name = 'phone/list.html'
    context_object_name = 'phone_list'

class EditPhoneView(UpdateView):
    model = PhoneModel
    form_class = PhoneUpdateForm
    template_name = 'phone/edit.html'
    success_url = reverse_lazy('phone:phone-list')

class DeletePhoneView(DeleteView):
    model = PhoneModel
    template_name = 'phone/delete.html'
    context_object_name = 'phonedel'
    success_url = reverse_lazy('phone:phone-list')

def call_add(request,pk=None):
    form = CallForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.phone_id = PhoneModel.objects.filter(phone_id=pk).first()
        instance.duration = instance.end_time - instance.start_time
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, template_name='phone/add-call.html', context=context)

def call_list(request,pk=None):
    call_list_queryset = CallHistoryModel.objects.filter(phone_id = pk)
    context = {'call_list':call_list_queryset}
    return render(request,template_name='phone/show-call.html',context=context)

def call_edit(request,pk=None):
    call_list_queryset = CallHistoryModel.objects.filter(id=pk).first()
    initial = {'start_time':call_list_queryset.start_time,'end_time':call_list_queryset.end_time}
    form = CallForm(request.POST or None,initial=initial)
    if form.is_valid():
        instance = form.save(commit=False)
        call_list_queryset.start_time = instance.start_time
        call_list_queryset.end_time = instance.end_time
        call_list_queryset.duration = instance.end_time - instance.start_time
        call_list_queryset.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, template_name='phone/edit-call.html', context=context)








