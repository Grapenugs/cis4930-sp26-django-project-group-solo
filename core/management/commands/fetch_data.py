from django.core.management.base import BaseCommand
from django.db import transaction
import requests
from core.models import Repository


class Command(BaseCommand):
    help = 'Fetch GitHub repositories'

    def handle(self, *args, **kwargs):
        BASE_URL = "https://api.github.com/search/repositories"

        query = "python"
        per_page = 30

        for page in range(1, 4):  # fetch 3 pages
            try:
                response = requests.get(
                    BASE_URL,
                    params={
                        "q": query,
                        "sort": "stars",
                        "order": "desc",
                        "per_page": per_page,
                        "page": page
                    },
                    timeout=10
                )
                #Raise any potential exceptions automatically
                response.raise_for_status()
                data = response.json()

                #Add repos to the database
                with transaction.atomic():
                    for repo in data['items']:
                        Repository.objects.update_or_create(
                            defaults={
                                'name': repo['name'],
                                'url': repo['html_url'],
                                'stars': repo['stargazers_count'],
                                'language': repo['language'],
                                'fetched_at': repo['created_at']
                            }
                        )

                self.stdout.write(f"Fetched page {page}")

            except requests.exceptions.RequestException as e:
                self.stderr.write(f"Error: {e}")

