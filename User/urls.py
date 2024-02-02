from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view(),name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('deposit/', views.DepositMoneyView.as_view(), name='deposit'),
    path('adapt-pet/<int:id>', views.adapt_pet, name='adaptpet'),
    path('profile/', views.profileView, name='profile' ),
    path('update-profile/', views.update_profile, name='updateprofile' ),
    path('update-pass/', views.update_password, name='updatepassword' ),
    path('active/<uid64>/<token>/', views.activate, name='activate')
]