from django.shortcuts import render
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    template_name = 'main_page.html'

def home(request):
    if request.user.is_authenticated:
        avatar_url = request.user.avatar.url if request.user.avatar else None
    else:
        avatar_url = None

    return render(request, 'main_page.html', {'avatar_url': avatar_url})
