from django import forms
from .models import Track, Artist

class TrackForm(forms.ModelForm):
    new_artist = forms.CharField(
        required=False,
        label="Add new artist",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Track
        fields = [
            'name',
            'artist',
            'popularity',
            'danceability',
            'energy',
            'tempo',
            'track_genre',
        ]
    
    #Since artist is a foreign key ref, this allows to add a new name
    def save(self, commit=True):
        instance = super().save(commit=False)

        new_artist_name = self.cleaned_data.get('new_artist')

        if new_artist_name:
            artist, _ = Artist.objects.get_or_create(name=new_artist_name)
            instance.artist = artist

        if commit:
            instance.save()

        return instance
