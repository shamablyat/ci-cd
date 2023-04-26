from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TutorialSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
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

@api_view(['GET', 'POT', 'DELETE'])
def snippet_detail(request, pk):
    if request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
