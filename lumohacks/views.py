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
    has_hat = Gift.objects.filter(name='Hat', purchased=True).exists()
    has_bowtie = Gift.objects.filter(name='Bow Tie', purchased=True).exists()
    if has_bowtie and has_hat:
        cloth='both'
    elif has_bowtie:
        cloth = 'bow_tie'
    elif has_hat:
        cloth = 'hat'
    else:
        cloth = 'none'
    if Pet.objects.filter(auth_user__in=connections).exists():
        pet = Pet.objects.get(auth_user__in=connections)
        total_exp = pet.exp
        level = floor(total_exp/35) if pet.exp != 0 else 0
        remaining_exp = total_exp - 35*level
        level_exp = 35*(level+1)
        percentage = (float(remaining_exp)/level_exp)*100
    else:
        pet = None
        level = 0
        percentage = 0
    pet_user = PetUser.objects.get(auth_user=request.user)
    money = pet_user.money

    return render(request, template_name=template_name,
                  context={'pet': pet, 'money': money, 'level': int(level+1), 'percentage': percentage, 'cloth':cloth})

def cbt(request):
    template_name = 'cbt.html'
    user_activities = UserActivities.objects.filter(auth_user=request.user)
    connection = Connection.objects.get(Q(user_a=request.user)|Q(user_b=request.user))
    if connection.user_a == request.user:
        peer = connection.user_b
    else:
        peer = connection.user_a
    peer_activities = UserActivities.objects.filter(auth_user=peer)
    cbts_unanswered_by_both = Activity.objects.filter(type=1).exclude(useractivities__in=user_activities).exclude(useractivities__in=peer_activities)
    cbts_answered_by_peer = Activity.objects.filter(type=1, useractivities__in=peer_activities).exclude(
        useractivities__in=user_activities)

    return render(request, template_name=template_name, context={'cbts_unanswered_by_both':cbts_unanswered_by_both,
                                                                 'cbts_answered_by_peer':cbts_answered_by_peer})

def geo(request):
    template_name = 'geo.html'
    user_activities = UserActivities.objects.filter(auth_user=request.user)
    connection = Connection.objects.get(Q(user_a=request.user)|Q(user_b=request.user))
    if connection.user_a == request.user:
        peer = connection.user_b
    else:
        peer = connection.user_a
    peer_activities = UserActivities.objects.filter(auth_user=peer)
    cbts_unanswered_by_both = Activity.objects.filter(type=2).exclude(useractivities__in=user_activities).exclude(useractivities__in=peer_activities)
    cbts_answered_by_peer = Activity.objects.filter(type=2, useractivities__in=peer_activities).exclude(
        useractivities__in=user_activities)
    return render(request, template_name=template_name, context={'cbts_unanswered_by_both':cbts_unanswered_by_both,
                                                                 'cbts_answered_by_peer':cbts_answered_by_peer})


def map(request):
    template_name = 'map.html'
    return render(request, template_name=template_name)


def buy_gifts(request, gift_id):
    pet_user = PetUser.objects.get(auth_user=request.user)
    money = pet_user.money

    gift = Gift.objects.get(id=gift_id)
    gift_price = gift.price
    if money>=gift_price:
        gift.purchased = True
        gift.save()
        pet_user.money -= gift_price
        pet_user.save()
    return redirect('pet')


def store(request):
    template_name = 'store.html'
    pet_user = PetUser.objects.get(auth_user=request.user)
    money = pet_user.money
    gifts = Gift.objects.filter(purchased=False)
    return render(request, template_name=template_name,
                  context={'money': money, 'gifts':gifts})


def activity_detail(request, activity_id):
    template_name = 'activity_detail.html'
    activity = Activity.objects.get(id=activity_id)
    return render(request, template_name=template_name, context={'activity':activity})


def activity_done(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    user_activity = UserActivities.objects.create(auth_user=request.user, activity=activity, is_answered=True)
    user_activity.save()

    connection = Connection.objects.get(Q(user_a=request.user)|Q(user_b=request.user))
    if connection.user_a == request.user:
        peer = connection.user_b
    else:
        peer = connection.user_a

    if UserActivities.objects.filter(auth_user=peer, activity=activity).exists():
        multiplier = 2
    else:
        multiplier = 1


    pet_user = PetUser.objects.get(auth_user=request.user)
    pet_user.money += activity.money * multiplier
    pet_user.save()

    connections = Connection.objects.filter(Q(user_a=request.user)|Q(user_b=request.user))
    pet = Pet.objects.filter(auth_user=connections[0])[0]
    pet.exp += activity.experience * multiplier
    pet.save()
    return redirect('pet')
    # return render(request, template_name=template_name, context={'activity':activity})