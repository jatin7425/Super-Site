from django import forms
from django.contrib.auth.models import User
from .models import LearningEntry
from django_select2.forms import Select2MultipleWidget

class LearningEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['shared_with'].queryset = User.objects.exclude(id=user.id)
        else:
            self.fields['shared_with'].queryset = User.objects.none()
        
    class Meta:
        model = LearningEntry
        fields = ['title', 'content', 'shared_with']
        widgets = {
            'shared_with': Select2MultipleWidget(attrs={
                'data-minimum-input-length': 1,
                'class': 'w-full'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 rounded-lg focus:outline-none bg-gray-700 border-gray-600 focus:ring-2 focus:ring-blue-500 text-white'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 rounded-lg focus:outline-none bg-gray-700 border-gray-600 focus:ring-2 focus:ring-blue-500 h-32 text-white'
            }),
        }