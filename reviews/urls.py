from django.urls import path
from . import views
from .views import ReviewView

urlpatterns = {
    path('', ReviewView.as_view()),
    path('thank-you', views.thank_you)
}
