import datetime
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView, CreateView
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from IPython import embed

from blog.models import *
from blog.forms import *
# Create your views here.

class Minha_home(generic.TemplateView):
    template_name = "blog/home.html"

    def get(self, request, *args, **kwargs):
        context = super(Minha_home, self).get_context_data(**kwargs)
        obj = Post.objects.filter(data_criacao__lte=timezone.now())
        obj = obj.order_by('data_pub')
        context.update({
            'obj' : obj[:6]
        })
        return super(Minha_home, self).get( request, *args, **context)

class Minha_listagem(generic.ListView):
    template_name = "blog/list_post.html"
    model = Post

class Meu_detalhe(generic.DetailView):
    template_name = "blog/detalhe.html"
    context_object_name = 'post'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context.update({
            'form' : CommentForm()
        })

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.post = post
            obj.save()
            return HttpResponseRedirect(reverse('detalhe',  kwargs={'pk' : post.pk}))

class CriaFormView(CreateView):
    template_name = 'blog/form_create.html'
    ## formulario modelde
    form_class = MeuForm
    success_url = '/'


    def post(self, request, *args, **kwargs):
        self.object = None
        ## formulario preenchido 
        form = self.get_form()

        # from IPython import embed; embed()
        
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.autor = User.objects.get(email='bgmartins@ucs.br')
            return self.form_valid(instancia)
        else:
            for field in form.fields:
                if field in form.errors:
                    form.fields[field].widget.attrs['class'] += ' is-invalid'
                
            return self.form_invalid(form)

class EditaFormView(FormView):
    template_name = 'blog/form_edit.html'
    form_class = MeuForm
    success_url = '/posts/edit'

    def post(self, request, *args, **kwargs):

        return super(CriaFormView, self).post(request, *args, **kwargs)

