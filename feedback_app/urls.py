from django.urls import path
from .views import feedback_view, home, feedback_list


urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback_view, name='feedback'),
    path('all-feedbacks/', feedback_list, name='feedback_list')
]
