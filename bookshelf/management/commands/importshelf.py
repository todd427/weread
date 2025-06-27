# bookshelf/management/commands/importshelf.py
import json
from django.core.management.base import BaseCommand
from bookshelf.models import shelfBook

class Command(BaseCommand):
    help = "Import books from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, required=True, help='Path to the JSON file to import')

    def handle(self, *args, **options):
        json_file = options['file']
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        created = 0
        for entry in data:
            obj, made = shelfBook.objects.get_or_create(
                title=entry.get('title', '')[:300],
                author=entry.get('author', ''),
                defaults={
                    'user': entry.get('user', 'todd'),
                    'isbn': entry.get('isbn', ''),
                    'openlibrary_url': entry.get('openlibrary_url', ''),
                    'googlebooks_url': entry.get('googlebooks_url', ''),
                    'amazon_url': entry.get('amazon_url', ''),
                    'amazon_search_url': entry.get('amazon_search_url', ''),  # <-- Add this line
                    'date_acquired': entry.get('date_acquired', None),
                }
            )

            if made:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Imported {created} new books from {json_file}"))
