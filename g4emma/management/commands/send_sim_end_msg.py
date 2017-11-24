from django.core.management.base import BaseCommand, CommandError
from channels import Channel, Group

class Command(BaseCommand):
    help = 'Notify that one more simulation event has completed to update progress'

    def add_arguments(self, parser):
        parser.add_argument('userdir', nargs='+', type=str)

    def handle(self, *args, **options):
        # Extract channel name (userdir for unique channels)
        channel_name = str(options['userdir']).strip("[]'")
        # Send message
        Group(channel_name).send({
            'text': "end",
        })

        # Let user know it worked
        self.stdout.write(
            self.style.SUCCESS('Simultion end message sent.'))
