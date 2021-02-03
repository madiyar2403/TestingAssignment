from django.urls import include, path
from .views import people, people_detail

urlpatterns = [
    path('people/', people),
    path('people/<iin>/', people_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
