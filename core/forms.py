from django import forms

class contatoform(forms.Form):
    nome= forms.CharField(label='nome',max_length=100)
    email= forms.EmailField(label='email',max_length=100)
    assunto=forms.CharField(label='assunto',max_length=120)
    mensagem=forms.CharField(label='mensagem',widget=forms.Textarea())