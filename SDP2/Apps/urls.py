from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login, name='Login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('Explore', views.explore, name='Explore'),
    path('Aboutus', views.aboutus, name='Aboutus'),
    path('Booking', views.booking, name='Booking'),
    path('contact', views.contact, name='contact'),
    path('Profile', views.Profile, name='Profile'),
    path('logout', views.Logout, name='logout'),
    path('contact_list', views.contact_list, name='contact_list'),
    path('delete-read-contacts/', views.delete_read_contacts, name='delete_read_contacts'),
    path('booking_list', views.booking_list, name='booking_list'),
    path('delete-read-bookings/', views.delete_read_bookings, name='delete_read_bookings'),
    path('thanks/<str:email>/', views.thanks, name='thanks'),
    path('forgotpass/', views.forgotpass, name='forgotpass'),
    path('changepass/<token>', views.changepass, name='changepass'),
    path('customer1', views.customer1, name='customer1'),
    path('producer1', views.producer1, name='producer1'),
    path('jobBooking', views.jobBooking, name = 'jobBooking'),
        path('hostre', views.hostre, name = 'hostre'),
]
