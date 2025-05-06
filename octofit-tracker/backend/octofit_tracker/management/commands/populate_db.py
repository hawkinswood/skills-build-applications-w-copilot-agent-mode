from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", age=25)
        user2 = User.objects.create(email="user2@example.com", name="User Two", age=30)

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=150)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing morning yoga session.")
        Workout.objects.create(name="HIIT", description="High-intensity interval training.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))