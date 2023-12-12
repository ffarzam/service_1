import csv
from django.core.management.base import BaseCommand
from dumpdata.models import Raw


class Command(BaseCommand):
    help = 'Import data from CSV file into PostgreSQL database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            # for row in reader:
            #     Raw.objects.create(**row)
            obj = (Raw(**row) for row in reader)
            Raw.objects.bulk_create(obj)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
