from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    danceability = models.FloatField(default=0)
    energy = models.FloatField(default=0)
    
    tempo = models.FloatField(default=0)
    track_genre = models.CharField(max_length=100, null=True, blank=True)

    SOURCE_CHOICES = [
        ('csv', 'CSV Import'),
        ('api', 'API Fetch'),
    ]
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    
    def __str__(self):
        return f"{self.name} - {self.artist.name}"

class Repository(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100, null=True, blank=True)
    stars = models.IntegerField(default=0)
    url = models.URLField(unique=True)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Repository"
        verbose_name_plural = "Repositories"

