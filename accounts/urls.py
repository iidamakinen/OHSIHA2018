from django.urls import path
from . import views
from .views import list_events_event, create_event, update_event, delete_event


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('etusivu', list_events, name='list_events'),
    path('etusivu', list_events_event, name='list_events_event'),
    path('new', create_event, name='create_event'),
    path('update/<int:id>/', update_event, name='update_event'),
    path('delete/<int:id>/', delete_event, name='delete_event'),
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
    path('testi', views.testi, name='testi')
    # path('event', event, name='event')
]
