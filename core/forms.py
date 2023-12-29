from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'fullname', 'email', 'password1', 'password2']

    
    def __init__(self,  *args, **kwargs):
        super().__init__( *args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-full shadow border bg-transparent text-white block my-2'


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'w-full shadow border bg-transparent text-white block my-2'