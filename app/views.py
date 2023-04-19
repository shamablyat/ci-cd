from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


# Create your views here.

class MainView(ListView):
    template_name = 'index.html'
    model = CommentModel
    context_object_name = 'comment'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['users_comment'] = CommentFromUsers.objects.all()
        context['team'] = TeamModel.objects.all()
        context["catry"] = Cat.objects.all()
        context['design'] = DesignModel.objects.all()

        return context

