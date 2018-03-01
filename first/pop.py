import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')

import django

django.setup()

import random

from firstapp.models import Webpage, Topic, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['search', 'app', 'wlan', 'remote']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(category=top, url=fake_url, name=fake_name)[0]
        webpage.save()

        acc_rec = AccessRecord.objects.get_or_create(name=webpage,date=fake_date)


if __name__ == '__main__':
    print('pop')
    populate(15)
    print('complete')

