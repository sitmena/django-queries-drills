from operator import le
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import random
from queries.models import (
    Location, 
    Language,
    Company,
    Programmer,
    )

COMPANIES = [
    'AMAZON',
    'GOOGLE',
    'SITECH',
    'MICROSOFT',
    'PSI',
    'EXPEDIA',
    'ATYPON',
    'PWC',
]

LANGUAGES = [
    'Python',
    'Java',
    'JavaScript',
    'c++',
    'Android',
    'Swift',
    'Flutter',
    'Ruby',
    'C-Sharp',
]

LANGUAGE_TYPES = [
    'O',
    'F',
]
class Provider(faker.providers.BaseProvider):
    def company(self):
        return self.random_element(COMPANIES)
    
    def language(self):
        return self.random_element(LANGUAGES)
    
    def type(self):
        return self.random_element(LANGUAGE_TYPES)

class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        
        fake = Faker()
        fake.add_provider(Provider)

        for _ in range(1, 9):
            country = fake.country()
            city = fake.city()
            streat = fake.street_name()
            building_number = fake.building_number()
            branch_id = fake.ssn()
            Location.objects.create(
                country=country,
                city=city,
                municipality=f'{city}-munici',
                streat=streat,
                building_number=building_number,
                branch_id=branch_id
            )

        for i in range(1, 9):
            name = fake.unique.company()
            created_date = fake.date()
            
            Company.objects.create(
                name=name,
                created_date=created_date,
                location=Location.objects.get(id=i)  
            )
        

        for i in range(1, 10):
            name = fake.unique.language()
            created_date = fake.date()
            type = fake.type()
            descripton = fake.paragraph(nb_sentences=5)
            Language.objects.create(
                name=name,
                created_date=created_date,
                type=type,
                descripton=descripton
            )


        for i in range(30):
            name = fake.name()
            age = random.randint(22, 60)
            joined_date = fake.date()
            company = Company.objects.get(id=random.randint(1, 8))

            prog = Programmer.objects.create(
                name=name,
                age=age,
                joined_date=joined_date,
                company=company
            )

            langs = three_unique_languages()
            prog.languages.add(langs[0], langs[1], langs[2])

            prog.save()


def three_unique_languages():
    
    lang1 = random.randint(1, 9)
    lang2 = random.randint(1, 9)
    lang3 = random.randint(1, 9)

    while(lang1 == lang2) or (lang1 == lang3) or (lang2 == lang3):
        lang1 = random.randint(1, 9)
        lang2 = random.randint(1, 9)
        lang3 = random.randint(1, 9)
        
    return [lang1, lang2, lang3]