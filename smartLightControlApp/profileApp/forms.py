from django import forms
from django.utils.translation import gettext_lazy as _

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['access_token', 'company_domain']
        labels = {
            'access_token': _("Токен доступу"),
            'company_domain': _("Домен компанії")
        }


class ConsentForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['consent_for_data_collection']
