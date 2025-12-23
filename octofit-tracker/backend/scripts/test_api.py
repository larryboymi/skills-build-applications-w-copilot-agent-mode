import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.test import Client
from django.conf import settings

client = Client()

endpoints = [
    '/api/users/',
    '/api/teams/',
    '/api/activities/',
    '/api/workouts/',
    '/api/leaderboard/',
]

print('Using ALLOWED_HOSTS:', settings.ALLOWED_HOSTS)
for ep in endpoints:
    r = client.get(ep)
    print(f'GET {ep} -> {r.status_code}')
    try:
        print(r.json())
    except Exception:
        print(r.content[:200])
