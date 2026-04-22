from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Track
from .forms import TrackForm
from django.urls import reverse_lazy
import json
import pandas as pd

class TrackListView(ListView):
    model = Track
    template_name = "core/list.html"
    context_object_name = "tracks"  #name of the data inside the template
    paginate_by = 20 #show only 20 tracks per page

class TrackDetailView(DetailView):
    model = Track
    template_name = 'core/detail.html'
    context_object_name = 'track'

def home(request):
    return render(request, 'core/home.html')

class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('track_list')

class TrackUpdateView(UpdateView):
    model = Track
    form_class = TrackForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('track_list')

class TrackDeleteView(DeleteView):
    model = Track
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('track_list')

#Used for analytics dashboard
def analytics(request):
    #Create a pandas dataframe from of Track data
    qs = Track.objects.values(
        'track_genre',
        'popularity',
        'danceability',
        'energy',
        'tempo'
    )

    df = pd.DataFrame(list(qs))

    # Avg popularity by genre
    genre_avg = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)

    genre_chart = {
        'labels': genre_avg.index.tolist(),
        'values': genre_avg.values.tolist()
    }

    #Avg energy by genre
    energy_avg = df.groupby('track_genre')['energy'].mean().head(10)

    energy_chart = {
        'labels': energy_avg.index.tolist(),
        'values': energy_avg.values.tolist()
    }

    #Avg danceability by genre
    dance_avg = df.groupby('track_genre')['danceability'].mean().head(10)

    dance_chart = {
        'labels': dance_avg.index.tolist(),
        'values': dance_avg.values.tolist()
    }

    #Summary of stats
    summary = df.describe().to_dict()

    return render(request, 'core/analytics.html', {
        'genre_chart': json.dumps(genre_chart),
        'energy_chart': json.dumps(energy_chart),
        'dance_chart': json.dumps(dance_chart),
        'summary': summary
    })

