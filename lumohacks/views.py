from django.shortcuts import render, redirect
from lumohacks.models import *
from django.db.models import Q
from math import log, floor, pow

def landing_page(request):
    template_name = 'landing_page.html'
    return render(request, template_name=template_name)

def pet_detail(request):
    template_name = 'pet.html'
    connections = Connection.objects.filter(Q(user_a=request.user)|Q(user_b=request.user))
    if Pet.objects.filter(auth_user__in=connections).exists():
        pet = Pet.objects.get(auth_user__in=connections)
        total_exp = pet.exp
        level = floor(total_exp/10) if pet.exp != 0 else 0
        remaining_exp = total_exp - 10*level
        level_exp = 10*(level+1)
        percentage = (float(remaining_exp)/level_exp)*100
    else:
        pet = None
        level = 0
        percentage = 0
    pet_user = PetUser.objects.get(auth_user=request.user)
    money = pet_user.money

    return render(request, template_name=template_name,
                  context={'pet': pet, 'money': money, 'level': level, 'percentage': percentage})

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
    pet_user = PetUser.objects.get(auth_user=request.user)
    pet_user.money += activity.money
    pet_user.save()

    connections = Connection.objects.filter(Q(user_a=request.user)|Q(user_b=request.user))
    pet = Pet.objects.filter(auth_user=connections[0])[0]
    pet.exp += activity.experience
    pet.save()
    return redirect('pet')
    # return render(request, template_name=template_name, context={'activity':activity})