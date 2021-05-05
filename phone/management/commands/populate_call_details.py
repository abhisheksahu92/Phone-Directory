from django.core.management.base import BaseCommand
from datetime import timedelta
from faker import Faker
from phone.models import PhoneModel,CallHistoryModel
from random import randint
from django.utils.timezone import make_aware


class Command(BaseCommand):
    help = 'Seed the Call Details database'

    def add_arguments(self, parser):
        parser.add_argument('--call',
                            default=10,
                            type=int,
                            help='The number of call details you want to create.')

    def handle(self, *args, **kwargs):
        try:
            phone_ids = PhoneModel.objects.all()
            fake = Faker()
            for phone_id in phone_ids:
                for x in range(kwargs['call']):
                    start_time = fake.date_time_this_year()
                    end_time = start_time + timedelta(hours=randint(00, 1), minutes=randint(00, 60),
                                                      seconds=randint(00, 60))
                    duration = end_time - start_time
                    CallHistoryModel.objects.create(phone_id=phone_id,
                                                    start_time=make_aware(start_time),
                                                    end_time=make_aware(end_time),
                                                    duration=duration)

        except Exception as e:
            print(e)

