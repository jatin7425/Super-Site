from django import forms
from django.conf import settings
from django.utils.module_loading import import_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.'
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for all fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'autocomplete': 'off'
            })
        
        # Specific field customizations
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'your.email@example.com'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Create a password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Re-enter your password'
        })

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Get all validators except UserAttributeSimilarityValidator
        filtered_validators = []
        for validator_dict in settings.AUTH_PASSWORD_VALIDATORS:
            validator_class = import_string(validator_dict['NAME'])
            if validator_class is UserAttributeSimilarityValidator:
                continue
            validator = validator_class(**validator_dict.get('OPTIONS', {}))
            filtered_validators.append(validator)
        
        try:
            validate_password(
                password1,
                self.instance,
                password_validators=filtered_validators
            )
        except ValidationError as e:
            self.add_error('password1', e)
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user