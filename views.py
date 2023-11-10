from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Record, CD, Cassette, Equipment
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class MyView(generic.View):
    def get(self, request):
        return render(request, 'recordrental/my_template.html')

def index(request):
    num_records = Record.objects.all().count()
    num_cds = CD.objects.all().count()
    num_cassettes = Cassette.objects.all().count()
    num_equipment = Equipment.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_records': num_records,
        'num_cds': num_cds,
        'num_cassettes': num_cassettes,
        'num_equipment': num_equipment,
        'num_visits': num_visits,
    }

    return render(request, 'recordrental/index.html', context=context)

def recordrental(request):
    return render(request, 'recordrental/recordrental.html')

class RecordListView(generic.ListView):
    model = Record
    template_name = 'recordrental/record_list.html'
    context_object_name = 'record_list'
    paginate_by = 5

class RecordDetailView(generic.DetailView):
    model = Record
    template_name = 'recordrental/record_detail.html'

class CassetteListView(generic.ListView):
    model = Cassette
    template_name = 'recordrental/cassette_list.html'
    context_object_name = 'cassette_list'
    paginate_by = 5

class CassetteDetailView(generic.DetailView):
    model = Cassette
    template_name = 'recordrental/cassette_detail.html'

class EquipmentListView(generic.ListView):
    model = Equipment
    template_name = 'recordrental/equipment_list.html'
    context_object_name = 'equipment_list'
    paginate_by = 5

class EquipmentDetailView(generic.DetailView):
    model = Equipment
    template_name = 'recordrental/equipment_detail.html'

class CDListView(generic.ListView):
    model = CD
    template_name = 'recordrental/cd_list.html'
    context_object_name = 'cd_list'
    paginate_by = 5

class CDDetailView(generic.DetailView):
    model = CD
    template_name = 'recordrental/cd_detail.html'
    context_object_name = 'cd'

class MyLoginView(LoginView):
    template_name = 'myapp/login.html'  
    success_url = reverse_lazy('myapp:index')  

class IndexView(TemplateView):
    template_name = 'myapp/index.html'
