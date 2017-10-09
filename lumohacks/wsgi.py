"""
WSGI config for lumohacks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/home/ubuntu/lumohacks-17/lumohacks')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ubuntu/lumohacks-17/ENV/Lib/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lumohacks.settings")

application = get_wsgi_application()
