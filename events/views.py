from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event  # Import the Event model
@login_required

def event_list(request):
    events = Event.objects.all()  # Fetch all events from DB
    return render(request, 'events/event_list.html', {'events': events})  # Pass events to template
