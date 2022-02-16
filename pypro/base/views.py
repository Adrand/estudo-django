from django.shortcuts import render


# Create your views here.


def home(request):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 251224475}
    return render(request, 'base/home.html', context={'video': video})
