from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView, DeleteView, CreateView
from .forms import CustomUserForm, UserAddressForm
from .models import UserAddress, CustomUser

class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class AddressesView(LoginRequiredMixin, ListView):
    model = UserAddress
    template_name = 'user/addresses.html'
    context_object_name = 'user_addresses'

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('user-addresses')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserAddressForm()
        return context


class DeleteAddressView(LoginRequiredMixin, DeleteView):
    model = UserAddress
    success_url = reverse_lazy('user-addresses')

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


class EditAddressView(LoginRequiredMixin, UpdateView):
    model = UserAddress
    form_class = UserAddressForm
    template_name = 'user/address.html'
    success_url = reverse_lazy('user-addresses')


class AddAddressView(LoginRequiredMixin, CreateView):
    model = UserAddress
    form_class = UserAddressForm
    template_name = 'user/address.html'
    success_url = reverse_lazy('user-addresses')

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        address.save()
        return super().form_valid(form)
