import csv
from django.core.management.base import BaseCommand
from core.models import Artist, Track
import os

class Command(BaseCommand):
    help = "Load Spotify CSV data into the database"

    def handle(self, *args, **kwargs):
     # Capture base directory where data/raw folder lives
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        file_path = f"{BASE_DIR}/data/raw/spotify.csv"
        

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0

            for row in reader:
                try:
                    #row = {k.strip(): v for k, v in row.items() if k}
                    #artist_name = (row.get('artists') or "").strip()
                    #track_name = (row.get('track_name') or "").strip()
                    artist_name = row.get('artists')
                    track_name = row.get('track_name')

                    if not artist_name or not track_name:
                        continue
                    # Some datasets have multiple artists separated by commas
                    artist_name = artist_name.split(",")[0].strip()

                    artist, _ = Artist.objects.get_or_create(name=artist_name)
                    Track.objects.update_or_create(
                        name = track_name,
                        artist = artist,
                        defaults = {
                            'popularity': int(row.get('popularity', 0)),
                            'danceability': float(row.get('danceability', 0)),
                            'energy': float(row.get('energy', 0)),
                            'source': 'csv',
                        }
                    )

                    count += 1

                except Exception as e:
                    self.stderr.write(f"Error: {e}")

            self.stdout.write(self.style.SUCCESS(f"Loaded {count} track"))
