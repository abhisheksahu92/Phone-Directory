import sys,os
from django.core.management.base import BaseCommand
from django.db import transaction

from phone.models import PhoneModel

class Command(BaseCommand):
    help = 'Delete the Post database'

    @transaction.atomic
    def handle(self,*args,**kwargs):
        PhoneModel.objects.all().delete()