from django.urls import path
from .views import *


urlpatterns=[
    path('dash',DashboardView.as_view(),name='dash'),
    path('add',AddStudentView.as_view(),name='add'),
    path('delete/<int:id>',DeleteStudentView.as_view(),name='delete'),
    path('edit/<int:id>',EditStudentView.as_view(),name='edit'),
    path('reg',RegView.as_view(),name='reg'),
    path('landing',LandingView.as_view(),name='landing')

]