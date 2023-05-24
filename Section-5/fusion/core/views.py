from typing import Any, Dict
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .models import Servico, Funcionario
from django.urls import reverse_lazy
from .forms import ContatoForm
from django.contrib import messages

class Teste404View(TemplateView):
    template_name = '404.html'

class Teste500View(TemplateView):
    template_name = '500.html'

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    
