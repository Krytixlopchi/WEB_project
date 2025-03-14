from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import User, Collection, NFT,Transaction, Image

admin.site.register(Image)
admin.site.register(User)
admin.site.register(Collection)
admin.site.register(NFT)
admin.site.register(Transaction)

