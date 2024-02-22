from django.shortcuts import render, redirect
from .forms import VolunteerForm
from django.http import HttpResponse
import csv
from .models import Volunteer

def volunteer_form(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the thank you page
            return redirect('thank_you_page')
    else:
        form = VolunteerForm()
    return render(request, 'form.html', {'form': form})

def thank_you_page(request):
    return render(request, 'thank_you.html')

def export_volunteers_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="volunteers.csv"'

    volunteers = Volunteer.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Full Name','Email', 'Year', 'Branch', 'Skills', 'Event', 'Reason'])

    for volunteer in volunteers:
        writer.writerow([volunteer.full_name, volunteer.year, volunteer.branch, volunteer.skills, volunteer.event, volunteer.reason])

    return response
