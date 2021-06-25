from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)
from django.urls import reverse_lazy
from .models import Incident

class IncidentListView(ListView):
  template_name = 'incidents/incident_list.html'
  model = Incident

class IncidentDetailView(DetailView):
  template_name = 'incidents/incident_detail.html'
  model = Incident

class IncidentCreateView(CreateView):
  template_name = 'incidents/incident_create.html'
  model = Incident
  fields = ['summary', 'reporter', 'detail']

class IncidentUpdateView(UpdateView):
  template_name = 'incidents/incident_view.html'
  model = Incident
  fields = ['summary', 'reporter', 'detail']

class IncidentDeleteView(DeleteView):
  template_name = 'incidents/incident_delete.html'
  model = Incident
  fields = ['summary', 'reporter', 'detail']
  succell_url = reverse_lazy('incident list')

  

