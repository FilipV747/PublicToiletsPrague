from django.core.management.base import BaseCommand
import json
from prague.models import Toilet
import uuid
import re

class Command(BaseCommand):
    def handle(self, *args, **options):
        path = 'prague/management/data/toilets_data.json'
        with open(path, encoding='UTF-8') as soubor:
            data = json.load(soubor)

            for item in data['features']:
                geometry = item['geometry']
                properties = item['properties']

                address = properties.get("ADRESA", None)
                if not address or re.match(r'^\s*$', address):
                    address = "Public WC"

                price = properties.get("CENA", None)
                if not price:
                    price = "Not Specified"

                schedule = properties.get("OTEVRENO", None)
                if not schedule:
                    schedule = "Not Specified"

                toilet, created = Toilet.objects.update_or_create(
                address=address,
                latitude=geometry["coordinates"][1],
                longitude=geometry["coordinates"][0],
                price=price,
                schedule=schedule,
            )

                toilet.slug = str(uuid.uuid4())[:5]
                toilet.save()



