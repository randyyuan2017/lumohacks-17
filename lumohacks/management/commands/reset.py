from django.core.management.base import BaseCommand, CommandError
from lumohacks.models import *

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for user_activities in UserActivities.objects.all():
            user_activities.delete()

        for pet in Pet.objects.all():
            pet.exp = 0
            pet.save()

        for user in PetUser.objects.all():
            user.money = 0
            user.save()

        for gift in Gift.objects.all():
            gift.purchased = False
            gift.save()


        self.stdout.write(self.style.SUCCESS('Successfully reset db'))