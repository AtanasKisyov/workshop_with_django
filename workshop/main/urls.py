from django.urls import path

from workshop.main.views import home, dashboard, unauthorized

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('unauthorized/', unauthorized, name='unauthorized')
]
