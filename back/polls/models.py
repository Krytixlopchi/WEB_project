from django.db import models

# Create your models here.
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet_address = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.username

class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NFT(models.Model):
    STATUS_CHOICES = [
        ('for_sale', 'For Sale'),
        ('sold', 'Sold'),
        ('delisted', 'Delisted'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_nfts")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="owned_nfts")
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name="nfts")
    metadata = models.URLField()  # IPFS/JSON URL
    price = models.DecimalField(max_digits=18, decimal_places=8, null=True, blank=True)
    minted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='for_sale')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nft = models.ForeignKey(NFT, on_delete=models.CASCADE, related_name="transactions")
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="sales")
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="purchases")
    amount = models.DecimalField(max_digits=18, decimal_places=8)
    tx_hash = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.tx_hash}"
