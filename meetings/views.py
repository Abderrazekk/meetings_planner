from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
from .forms import MeetingForm

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings/list.html', {'meetings': meetings})

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})

# Nouvelle vue pour ajouter une réunion
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la réunion dans la base de données db.sqlite3
            return redirect('meeting_list')  # Redirige vers la liste des réunions
    else:
        form = MeetingForm()
        
    return render(request, 'meetings/new.html', {'form': form})

def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect('meeting_list')
    return render(request, 'meetings/confirm_delete.html', {'meeting': meeting})