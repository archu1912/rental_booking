from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def helloView(request):
    return HttpResponse("Hello, World!")

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"
