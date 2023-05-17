from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto
from django.contrib import messages

from .models import Email

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        # print(f'Post: {request.POST}')
        if form.is_valid():
            # emailForm = Email(request.POST)
            # emailForm.nome = form.cleaned_data['nome']
            # emailForm.email = form.cleaned_data['email']
            # emailForm.assunto = form.cleaned_data['assunto']
            # emailForm.mensagem = form.cleaned_data['mensagem']
            # emailForm.full_clean() recommended when you not using a model form  
            # emailForm.save()
            
            form.send_mail()
            
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            # print(form.cleaned_data)

            # print('Mensagem enviada')
            # print(f'Nome:{nome}')
            # print(f'email:{email}')
            # print(f'assunto:{assunto}')
            # print(f'mensagem:{mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    print(f'Usuário: {request.user}')
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                # print(f'Post: {request.POST}')
                # prod = form.save(commit=False)
                # print(f'Nome: {prod.nome}')
                # print(f'Preço: {prod.preco}')
                # print(f'Estoque: {prod.estoque}')
                # print(f'Imagem: {prod.imagem}')

                form.save()

                messages.success(request, 'Produto salvo com sucesso!') 
                form = ProdutoModelForm()           
            else:
                messages.error(request, 'Erro ao salvar o produto!')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')