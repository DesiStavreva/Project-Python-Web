from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from django.utils.translation import gettext, gettext_lazy as _

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name',)

    password2 = forms.CharField(
        label=_("Repeat Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Repeat Password, please"),
    )

