from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = "polls"

urlpatterns = [
    path('nfts/', views.nft_list, name='nft_list'),
    path("nfts/<uuid:nft_id>/", views.nft_detail, name="nft_detail"),
    path("collections/<uuid:collection_id>/", views.collection_detail, name="collection_detail"),
    path('register/', views.user_registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
]








