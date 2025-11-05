from django.core.management.base import BaseCommand
from api.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Use pymongo for all test data population
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections to fully clear and remove indexes
        for coll in ['users', 'teams', 'activities', 'workouts', 'leaderboard']:
            db.drop_collection(coll)

        # Insert teams
        marvel_id = db['teams'].insert_one({'name': 'Marvel'}).inserted_id
        dc_id = db['teams'].insert_one({'name': 'DC'}).inserted_id

        # Insert users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': marvel_id},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_id},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team_id': dc_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id},
        ]
        user_ids = db['users'].insert_many(users).inserted_ids

        # Insert activities
        activities = []
        for uid in user_ids:
            activities.append({'user_id': uid, 'type': 'Running', 'duration': 30})
            activities.append({'user_id': uid, 'type': 'Cycling', 'duration': 45})
        db['activities'].insert_many(activities)

        # Insert workouts
        db['workouts'].insert_one({'name': 'Cardio Blast', 'description': 'High intensity cardio workout', 'suggested_for': user_ids})
        db['workouts'].insert_one({'name': 'Strength Training', 'description': 'Full body strength routine', 'suggested_for': user_ids})

        # Insert leaderboard
        db['leaderboard'].insert_one({'team_id': marvel_id, 'points': 100})
        db['leaderboard'].insert_one({'team_id': dc_id, 'points': 90})

        # After population, recreate unique index on users.email
        db['users'].create_index('email', unique=True)

        print('octofit_db populated with test superhero data')
