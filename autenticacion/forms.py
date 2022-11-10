from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from usuarios.models import usuarios
  
from django.contrib.auth import get_user_model
# from user.models import User
# User = get_user_model()

# class CustomUserCreationForm(UserCreationForm):  
    
#     # password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='Ingrese su contraseña')  
#     # password2 = forms.CharField(label='Contraseña (confirmación)', widget=forms.PasswordInput, help_text='Para verificar, introduzca la misma contraseña anterior.')  
#     first_name = forms.CharField(label='Nombre', min_length=3, max_length=150)  
#     last_name = forms.CharField(label='Apellido', min_length=3, max_length=150)  
#     # username = forms.CharField(label='Nombre de usuario', min_length=5, max_length=150, help_text='Requerido. 150 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_')  
#     email = forms.EmailField(label='Correo electrónico', help_text='Dirección de correo electrónico')  
#     cui = forms.IntegerField(label='CUI', help_text='Código Único de Identificación CUI')  
    
  
#     # def username_clean(self):  
#     #     username = self.cleaned_data['username'].lower()  
#     #     new = User.objects.filter(username = username)  
#     #     if new.count():  
#     #         raise ValidationError("Este usuario ya existe.")  
#     #     return username  
  
#     def get_first_name(self):  
#         first_name = self.cleaned_data['first_name'].lower()  
#         new = User.objects.filter(first_name = first_name)  
#         if new.count():  
#             raise ValidationError("Este usuario ya existe.")  
#         return first_name 

#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError("Este email ya se encuentra utilizado.")  
#         return email  
  
#     # def clean_password2(self):  
#     #     password1 = self.cleaned_data['password1']  
#     #     password2 = self.cleaned_data['password2']  
  
#     #     if password1 and password2 and password1 != password2:  
#     #         raise ValidationError("Las contraseñas no coinciden")  
#     #     return password2  
  
#     def save(self, commit = True):  
#         user = usuarios.objects.create(  
#             self.cleaned_data['first_name'],  
#             self.cleaned_data['last_name'],  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1'] 
#         )  
#         return user  

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'password1']
    
    cui = forms.IntegerField(label='CUI', help_text='Código Único de Identificación CUI')
    profile_imagen = forms.ImageField(label='Foto de perfil')

    
    # def email_clean(self):  
    #     email = self.cleaned_data['email'].lower()  
    #     new = User.objects.filter(email = email)  
    #     if new.count():  
    #         raise ValidationError("El email ya esta vinculado con otra cuenta, utiliza uno diferente.")  
    #     return email 


    def email_clean(self):
        # email = self.cleaned_data["email"]
        email = self.cleaned_data.get('email')
        new = User.objects.filter(email = email)  
        if new.count():  
            raise ValidationError("El email ya esta vinculado con otra cuenta, utiliza uno diferente.")  
        return email 
        # try:
        #     User._default_manager.get(email=email)
        # except User.DoesNotExist:
        #     return email
        # raise forms.ValidationError('email duplicado')

    # def email_clean(self):  
    #     email = self.cleaned_data.get('email')  
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError(u'El email ya esta vinculado con otra cuenta, utiliza uno diferente')
    #     return email 

# def clean_email(self):
#     email = self.cleaned_data["email"]
#     try:
#         User._default_manager.get(email=email)
#     except User.DoesNotExist:
#         return email
#     raise forms.ValidationError('El email ya esta vinculado con otra cuenta, utiliza uno diferente')
