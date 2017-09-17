from django.shortcuts import render, redirect
from lumohacks.models import *


def landing_page(request):
    template_name = 'landing_page.html'
    return render(request, template_name=template_name)

def pet_detail(request):
    template_name = 'pet.html'
    return render(request, template_name=template_name)

def cbt(request):
    template_name = 'cbt.html'
    user_activities = UserActivities.objects.filter(auth_user=request.user)
    unanswered_cbts = Activity.objects.filter(type=1).exclude(useractivities__in=user_activities)

    return render(request, template_name=template_name, context={'unanswered_cbts':unanswered_cbts})

def geo(request):
    template_name = 'geo.html'
    user_activities = UserActivities.objects.filter(auth_user=request.user)
    unanswered_geos = Activity.objects.filter(type=2).exclude(useractivities__in=user_activities)
    return render(request, template_name=template_name, context={'unanswered_geos':unanswered_geos})


def map(request):
    template_name = 'map.html'
    return render(request, template_name=template_name)


def store(request):
    template_name = 'store.html'
    return render(request, template_name=template_name)

def activity_detail(request, activity_id):
    template_name = 'activity_detail.html'
    activity = Activity.objects.get(id=activity_id)
    return render(request, template_name=template_name, context={'activity':activity})

def activity_done(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    try:
        user_activity = UserActivities.objects.create(auth_user=request.user, activity=activity, is_answered=True)
        user_activity.save()
    except Exception as e:
        print str(e)
    return redirect('pet')
    # return render(request, template_name=template_name, context={'activity':activity})