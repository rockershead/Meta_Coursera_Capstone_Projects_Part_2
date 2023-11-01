# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [

    # path('', views.index, name='index')

    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
]
