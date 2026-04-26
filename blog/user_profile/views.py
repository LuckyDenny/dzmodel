from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .utils import account_activation_token
from .forms import UserForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'user_profile/login.html')



def user_logout(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Підтвердіть ваш email'
            message = render_to_string('user_profile/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'user_profile/check_email.html')
    else:
        form = UserForm()

    return render(request, 'user_profile/register.html', {'form': form})

def profile(request):
    return render(request, 'user_profile/profile.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Дякуємо! Ваш email підтверджено. Тепер ви можете увійти.')
    else:
        return HttpResponse('Посилання для активації недійсне!')