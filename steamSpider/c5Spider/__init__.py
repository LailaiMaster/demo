import sys
import os
import django

sys.path.append('../../../web1')
os.environ['DJANGO_SETTINGS_MODULE'] = 'web1.settings'
django.setup()
