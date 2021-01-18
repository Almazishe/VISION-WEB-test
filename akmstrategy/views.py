from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

from .forms import DiscussTheProjectForm
from .models import Ad, Advantage, Goal

def base(request):
    form = DiscussTheProjectForm()
    simple_ads = Ad.objects.filter(ad_type=Ad.SIMPLE)
    dzen_ads = Ad.objects.filter(ad_type=Ad.DZEN)
    advantages = Advantage.objects.all()
    goals = Goal.objects.all()

    if request.method == 'POST':
        form = DiscussTheProjectForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['name'] + " - " + form.cleaned_data['phone'] + "\n" + form.cleaned_data['description']
            send_mail(
                'Обсудить проект',
                message,
                'someone@gmail.com',
                ['someone@gmail.com'],
                fail_silently=False,
            )
    context = {
        'form': form,
        'simple_ads': simple_ads,
        'dzen_ads': dzen_ads,
        'advantages': advantages,
        'goals': goals,
        'left': Advantage.LEFT,
        'right': Advantage.RIGHT,
    }
    return render(request, 'base.html', context)