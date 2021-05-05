from django import forms
from .models import PhoneModel,CallHistoryModel

class DateInput(forms.DateInput):
    input_type = 'date'

class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        if len(str(phone)) != 10:
            raise forms.ValidationError('Please Enter correct phone number.')
        elif PhoneModel.objects.filter(phone=phone).exists():
            raise forms.ValidationError('Phone number already exists.')
        elif PhoneModel.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

class PhoneUpdateForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        exclude = ['phone','email']

class DatetimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d %H:%M:%S"
        super().__init__(**kwargs)


class CallForm(forms.ModelForm):
    class Meta:
        model = CallHistoryModel
        fields =  ['start_time','end_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_time"].widget = DatetimeInput()
        self.fields["start_time"].input_formats = ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
        self.fields["end_time"].widget = DatetimeInput()
        self.fields["end_time"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]



