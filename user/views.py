from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm, UserAddressForm
from .models import UserAddress

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'user/profile.html', {'form': form})

@login_required
def addresses_view(request):
    user_addresses = UserAddress.objects.filter(user=request.user)
    form = UserAddressForm()

    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()

    return render(request, 'user/addresses.html', {'user_addresses': user_addresses, 'form': form})

@login_required
def delete_address_view(request, pk):
    address = get_object_or_404(UserAddress, pk=pk, user=request.user)
    if request.method == 'POST':
        address.delete()
        return redirect('addresses')

def edit_address_view(request, pk):
    address = get_object_or_404(UserAddress, pk=pk)
    if request.method == 'POST':
        form = UserAddressForm(request.POST or None, instance=address)
        if form.is_valid():
            form.save()
            return redirect('addresses')
    else:
        form = UserAddressForm(instance=address)

    return render(request, 'user/address.html', {'form': form, 'address': address})

def add_address_view(request):
    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('addresses')
        else:
            form = UserAddressForm()

    return render(request, 'user/address.html', {'form': form})
