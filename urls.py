from django.urls import path
from . import views

app_name = 'recordrental'

urlpatterns = [
    path('', views.index, name='index'),
    path('recordrental/', views.recordrental, name='recordrental'),
    path('records/', views.RecordListView.as_view(), name='record-list'),
    path('records/<int:pk>/', views.RecordDetailView.as_view(), name='record-detail'),
    path('cassettes/', views.CassetteListView.as_view(), name='cassette-list'),
    path('cassettes/<int:pk>/', views.CassetteDetailView.as_view(), name='cassette-detail'),
    path('equipment/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('cds/', views.CDListView.as_view(), name='cd-list'),
    path('cds/<int:pk>/', views.CDDetailView.as_view(), name='cd-detail'),
]
