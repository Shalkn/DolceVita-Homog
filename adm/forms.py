from django import forms
from adm.models import Produtos

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Endereço de E-mail",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Digite seu e-mail'
        })
    )
    
    new_password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Digite sua nova senha'})
    )
    new_password2 = forms.CharField(
        label="Confirme sua Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirme sua nova senha'})
    )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            'nome', 
            'descricao', 
            'preco', 
            'peso', 
            'status',
            'imagem'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
