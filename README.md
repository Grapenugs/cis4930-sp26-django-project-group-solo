#  Music & GitHub Analytics Dashboard (Django Project)

##  Project Overview
This project is a full-stack Django web application that integrates a Spotify Tracks dataset (from Kaggle) with live GitHub repository data using the GitHub API. The application provides a navigable web interface for CRUD operations, analytics dashboards, and live data ingestion.

It demonstrates end-to-end web development including Django ORM modeling, REST API integration, data analytics with Pandas, and interactive visualization using Chart.js and Bootstrap 5.

---

##  Group Members
Jack Norton

---

##  Data Sources

###  Spotify Dataset (Project 1)
- Source: Kaggle Spotify Tracks Dataset  
- Contains: track metadata including genre, popularity, energy, danceability, etc.

###  GitHub API (Project 2)
- Endpoint: https://api.github.com/search/repositories
- Fetches: repositories sorted by stars, language, and metadata


## Features

###  Pages
- Home page with navigation
- Track list view (paginated)
- Track detail view
- Create / Edit / Delete tracks (CRUD)
- Analytics dashboard

---

###  Spotify Track Management
- Full CRUD operations using Django ORM
- ModelForm with validation
- Admin panel customization
- CSV data loaded using management command (`seed_data`)


###  GitHub API Integration
- Management command: `fetch_data`
- Fetches repositories from GitHub API
- Stores data using Django ORM (`update_or_create`)
- Prevents duplicate entries
- Supports pagination and error handling


###  Analytics Dashboard
- Built using Pandas + Django ORM
- Includes:
  - Average popularity by genre
  - Average energy and danceability
  - GitHub repository language distribution
  - Average stars by programming language
- Visualized using Chart.js:
  - Bar charts
  - Pie charts
  - Multi-dataset comparisons
- Summary statistics table (mean, min, max)


##  Frontend
- Bootstrap 5 responsive UI
- Navbar with navigation links
- Bootstrap tables for data display
- Bootstrap forms for CRUD operations
- Custom CSS overrides in `static/css/style.css`
- Chart.js interactive dashboards


##  Tech Stack
- Python 3.9
- Django
- Pandas
- Chart.js
- Bootstrap 5
- GitHub API
- SQLite (development)


##  Project Structure


---

## Setup Instructions

### 1. Clone repository
```bash
git clone <repo-url>
cd cis4930-sp26-django-project-group-XX

### Install dependencies
pip install -r requirements.txt

### Run migrations:
python manage.py makemigrations
python manage.py migrate

#Load spotify dataset:
python manage.py seed_data

#Fetch github data:
python manage.py fetch_data

# Runserver
python manage.py runserver


System check identified 7 issues (0 silenced).
