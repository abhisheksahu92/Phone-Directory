from django.contrib import admin
from .models import PhoneModel,CallHistoryModel
# Register your models here.

@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone_id','first_name','middle_name','last_name','phone','email','gender']

@admin.register(CallHistoryModel)
class CallHistoryAdmin(admin.ModelAdmin):
    list_display = ['phone_id','start_time','end_time']