from django_countries import countries
from django.core.management.base import BaseCommand
from faker import Faker
from random import randint
from phone.models import PhoneModel

class Command(BaseCommand):
    help = 'Seed the Phone database'

    def add_arguments(self, parser):
        parser.add_argument('--users',
                            default=50,
                            type=int,
                            help='The number of users you want to create.')

    def handle(self,*args,**kwargs):
        fake = Faker()
        list_of_countries = []
        for code, name in list(countries):
            list_of_countries.append(code)
        try:
            for x in range(kwargs['users']):
                name = fake.name()
                first_name,last_name = name.split(maxsplit=1)
                phone = randint(1000000000, 9999999999)
                email = fake.free_email()
                gender = fake.random_element(['Male','Female'])
                date_of_birth = fake.date_of_birth()
                aadhaar_id = randint(100000000000, 999999999999)
                country = fake.random_element(list_of_countries)
                PhoneModel.objects.create(first_name=first_name,
                                          last_name=last_name,
                                          phone=phone,
                                          email=email,
                                          gender=gender,
                                          date_of_birth=date_of_birth,
                                          aadhaar_id=aadhaar_id,
                                          country=country)
        except Exception as e:
            print(e)


