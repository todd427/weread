# weread/management/commands/deletebooks.py
from django.core.management.base import BaseCommand
from weread.models import Book

class Command(BaseCommand):
    help = "Bulk delete Book records."

    def add_arguments(self, parser):
        parser.add_argument('--user', type=str, help="Delete books by user.")
        parser.add_argument('--author', type=str, help="Delete books by author (substring match).")
        parser.add_argument('--title', type=str, help="Delete books by title (substring match).")
        parser.add_argument('--all', action='store_true', help="Delete ALL books (no undo!).")

    def handle(self, *args, **options):
        qs = Book.objects.all()

        if options['all']:
            count = qs.count()
            confirm = input(f"Are you sure you want to delete ALL {count} books? Type 'yes' to confirm: ")
            if confirm.strip().lower() == 'yes':
                qs.delete()
                self.stdout.write(self.style.WARNING(f"Deleted ALL {count} books."))
            else:
                self.stdout.write(self.style.ERROR("Cancelled."))
            return

        if options['user']:
            qs = qs.filter(user=options['user'])
        if options['author']:
            qs = qs.filter(author__icontains=options['author'])
        if options['title']:
            qs = qs.filter(title__icontains=options['title'])

        count = qs.count()
        if count == 0:
            self.stdout.write(self.style.WARNING("No books matched your criteria."))
            return

        confirm = input(f"Delete {count} books? Type 'yes' to confirm: ")
        if confirm.strip().lower() == 'yes':
            qs.delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted {count} books."))
        else:
            self.stdout.write(self.style.ERROR("Cancelled."))
