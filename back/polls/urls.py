from django.urls import path
from . import views

app_name = "marketplace"

urlpatterns = [
    path('nfts/', views.nft_list, name='nft_list'),
    path("nfts/<uuid:nft_id>/", views.nft_detail, name="nft_detail"),
    path("collections/<uuid:collection_id>/", views.collection_detail, name="collection_detail"),
    path('register/', views.user_registration, name='register')
]



