from pathlib import Path

from decouple import config

BASE_DIR = Path().parent / 'pythonnobrasil'

GOOGLE_API_AUTH = config('GOOGLE_API_AUTH', default='google_auth.json')
GOOGLE_API_CALENDAR_ID = config('GOOGLE_API_CALENDAR_ID')

NETLIFY_TOKEN = config('NETLIFY_TOKEN')
NETLIFY_SITE_ID = config('NETLIFY_SITE_ID')
NETLIFY_API = config('NETLIFY_API')
