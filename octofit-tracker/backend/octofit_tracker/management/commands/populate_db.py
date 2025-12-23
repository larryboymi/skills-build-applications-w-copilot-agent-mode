from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', username='Ironman', team=marvel)
        spiderman = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, activity_type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=superman, activity_type='Yoga', duration=20, date=timezone.now().date())

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body workout')
        squats = Workout.objects.create(name='Squats', description='Lower body workout')
        pushups.suggested_for.set([ironman, batman])
        squats.suggested_for.set([spiderman, superman])

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=120)
        Leaderboard.objects.create(user=spiderman, points=110)
        Leaderboard.objects.create(user=batman, points=130)
        Leaderboard.objects.create(user=superman, points=125)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db!'))
