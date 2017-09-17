__author__ = 'parminder'

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db.models import Q
from django.contrib.auth.models import User, Group

# This management command will show total number of patients for each doctor
class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--reset',
                    action='store_true',
                    dest='stats',
                    default=False,
                    help='Doctors stats'),

    )

    def handle(self, *args, **options):
        if options['stats']:
            self.stats()
            self.stdout.write('*Successfully retrieved doctor stats')
        else:
            print "usage: python manage.py setup --help "

    def stats(self):
        list_one = ['ceridwen.lloyd@sundoctors.com.au',
                    'drsiggs@gmail.com',
                    'lvanmac@hotmail.com',
                    'dr.jonny.levy@gmail.com',]

        for list in list_one:
            try:
                user = User.objects.get(email=list)
                patients = get_objects_for_user(user, 'view_patient', klass=Patient)
                print list + " has: " + str(patients.count()) + " patients"
                images = Image.objects.filter(sent_by_user__email=list_one)
                print "Images Upload by Doctor: " + str(len(images))

            except:
                print "Doctor not found into system: " + str(list)
