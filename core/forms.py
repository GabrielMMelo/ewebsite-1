from django import forms

class ContatoForm(forms.Form):
	nome = forms.CharField(label='* Nome', required=True)
	email = forms.EmailField(label='* E-mail', required=True)
	assunto = forms.CharField(label='* Assunto', required=True)
	mensagem = forms.CharField(label='* Mensagem', widget=forms.Textarea(), required=True)

# utilizar model form depois
class ComentarioForm(forms.Form):
	nome = forms.CharField(label='* Nome', required=True)
	email = forms.CharField(label='* E-mail', required=True)
	comentario = forms.CharField(label='* Comentário', widget=forms.Textarea(), required=True)
