from .models import Movies,Profile,Comment
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['title','author','description','year','genre','poster']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Назва фільму'}),
            'author': forms.TextInput(attrs={'class':'form-control','placeholder':'Автор'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Опис'}),
            'year': forms.NumberInput(attrs={'class':'form-control','placeholder':'Рік'}),
            'genre': forms.TextInput(attrs={'class':'form-control','placeholder':'Жанр'}),
            'poster': forms.ClearableFileInput(attrs={'class':'form-control'})
        }
class RegisterForm(UserCreationForm):
    first_name= forms.CharField(max_length=20,required=True,label='Ім\'я',
        widget=forms.TextInput(attrs={'placeholder':"Ваше ім'я",'class':'form-input'})),
    last_name = forms.CharField(max_length=20,required=True,label='Прізвище',
        widget=forms.TextInput(attrs={'placeholder':"Ваше прізвище",'class':'form-input'}))
    email = forms.EmailField(required=True,label='Email',
        widget=forms.EmailInput(attrs={'placeholder':'your@gmail.com','class':'form-input'}))
    username = forms.CharField(label='Логін',
        widget=forms.TextInput(attrs={'placeholder':'Оберіть логін','class':'form-input'}))
    password1 =forms.CharField(label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder':'Мінімум 8 символів','class':'form-input'})) 
    password2 = forms.CharField(label='Підтвердження паролю',
        widget=forms.PasswordInput(attrs={'placeholder':'Повторіть пароль','class':'form-input'}))
    class Meta:
        model = User
        fields=('first_name',"last_name",'email','username','password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Цей email вже використовується')
        return email
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логін',
        widget=forms.TextInput(attrs={'placeholder':'Ваш логін','class':'form-input'}))
    password = forms.CharField(label='Логін',
        widget=forms.PasswordInput(attrs={'placeholder':'Ваш пароль','class':'form-input'}))
    
class ProfileForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20,required=True,label="Ім'я",
        widget=forms.TextInput(attrs={'class':'form-input'}))
    last_name = forms.CharField(max_length=30,required=False,label='Прізвище',
        widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(required=True,label='Email',
        widget=forms.EmailInput(attrs={'class':'form-input'}))
    class Meta:
        model = Profile
        fields = ('bio','avatar','avatar_color')
        labels = {'bio':'Про себе','avatar':'Фото профілю','avatar_color':'Колір аватару'}
        widgets ={
            'bio':forms.Textarea(attrs={'class':'form-input','rows':'4','placeholder':'Про себе'}),
            'avatar':forms.FileInput(attrs={'class':'form-input-file'}),
            'avatar_color':forms.TextInput(attrs={'type':'color','class':'form-color'})
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Залиште ваш коментар...'
            })
        }
        labels = {
            'text': 'Коментар'  
        }