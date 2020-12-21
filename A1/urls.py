from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
        path('', home, name='home'),
        path('login/', loginpage, name='login'),
        path('register/', registerpage, name='register'),
        path('logout/', logoutpage, name='logout'),

        path('product/', Prodects, name='product'),
        path('user/' , userpage , name='user-page'),
        path('customer/<str:pk>', Customers, name='customer'),
        path('create_order/<str:pk>', createOrder, name='create_order'),
        path('update_order/<str:pk>', updateOrder, name='update_order'),
        path('delete/<str:pk>', deleteOrder, name='delete_order'),
        path('account/', account_settings, name='account') ,

        path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html' ) , name = 'password_reset'),
        path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html') ,name = 'password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html') , name = 'password_reset_confirm'),
        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_send.html') , name = 'password_reset_complete'),

]
