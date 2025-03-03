from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import NFT, Collection, User

def nft_list(request):
    nfts = NFT.objects.all()
    return render(request, "polls/nft_list.html", {"nfts": nfts})

def nft_detail(request, nft_id):
    """Детальна інформація про NFT"""
    nft = get_object_or_404(NFT, id=nft_id)
    return render(request, "nft_detail.html", {"nft": nft})

def collection_detail(request, collection_id):
    """Детальна інформація про колекцію NFT"""
    collection = get_object_or_404(Collection, id=collection_id)
    return render(request, "collection_detail.html", {"collection": collection})

from django.shortcuts import render, redirect
from django.contrib import messages  # Для повідомлень
from .forms import UserRegistrationForm
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Зберігаємо нового користувача
            messages.success(request, 'Your account has been created successfully!')
            # Перенаправляємо на сторінку входу
    else:
        form = UserRegistrationForm()

    return render(request, 'polls/register.html', {'form': form})