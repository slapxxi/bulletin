from django import forms

from .models import User


class UserCreationForm(forms.ModelForm):
  error_messages = {
    'password_mismatch': 'The two password fields did not match.',
    'missing_email': 'Email is required.',
  }

  password = forms.CharField(widget=forms.PasswordInput)
  password_confirmation = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('username', 'email')

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if not email:
      raise forms.ValidationError(self.error_messages['missing_email'], code='missing_email')
    return email

  def clean_password_confirmation(self):
    password = self.cleaned_data.get("password")
    password_confirmation = self.cleaned_data.get("password_confirmation")
    if password and password_confirmation and password != password_confirmation:
        raise forms.ValidationError(
            self.error_messages['password_mismatch'],
            code='password_mismatch',
        )
    return password_confirmation

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password"])
    if commit:
        user.save()
    return user
