from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='密码')

    class Meta:
        model = User
        fields = ['username', 'password', 'student_id', 'name', 'email', 'phone', 'gender', 'age', 'hobby']
        widgets = {
            'hobby': forms.Textarea(attrs={'rows': 2}),
        }