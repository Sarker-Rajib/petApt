from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import CreateUserForm, DepositMoney, UpdateUser
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from Pets.models import Pet
from .models import AdaptPet
from datetime import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

class CreateUserView(FormView):
    form_class = CreateUserForm
    template_name = 'user_temp/register-form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        

        confirm_link = f'http://127.0.0.1:8000/user/active/{uid}/{token}'
        email_subject = 'Please Confirm Your Email'
        email_body = render_to_string('user_temp/confirm-email.html', {'confirm_link': confirm_link})
        
        email = EmailMultiAlternatives(email_subject, '', to=[user.email])
        email.attach_alternative(email_body, 'text/html')
        email.send()
        messages.success('Please Check Your Email')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid.")
        return super().form_invalid(form)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('login')
    
    else:
        return redirect('register')

class UserLoginView(LoginView):
    template_name = 'user_temp/login-form.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogOUt(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
    
class DepositMoneyView(FormView):
    form_class = DepositMoney
    template_name = 'user_temp/deposit-form.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.depositAccount

        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        return super().form_valid(form)

def profileView(request):
    user=request.user
    adaptedPets = AdaptPet.objects.filter(adaptedBy=user)
    return render(request, 'user_temp/profile.html', {'adaptedPets': adaptedPets, 'user' : user})

def update_profile(request):
    if request.method == 'POST':
        updateForm = UpdateUser(request.POST, instance = request.user)
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, 'User Created Successfully')
            return redirect('profile')
    else:
        updateForm = UpdateUser(instance = request.user)
        return render(request, 'user_temp/update-form.html', {'form':updateForm, 'title' : 'Update User Data'})

def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Updated Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, 'user_temp/update-form.html', {'form': form, 'title' : 'Update Password'})

def adapt_pet(request, id):
    target_pet = Pet.objects.get(pk=id)
    price = target_pet.adapt_price
    account = request.user.depositAccount
    balance = account.balance

    if price > balance:
        messages.warning(request, "You dont have sufficient Money.")
        return redirect(f'/user/pet-details/{id}')
    
    else:
        AdaptPet.objects.create(pet=target_pet, adaptedBy=request.user, timestamp = datetime.now())
        request.user.depositAccount.balance -= price
        request.user.depositAccount.save()
        return redirect('home')
