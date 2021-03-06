import os

from django.core.exceptions import ValidationError
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from faceverifier.multiforms import MultiFormsView
from mysite.settings import MEDIA_ROOT
from .models import UserDetails, UserAPIKey, UserImages
from .forms import LoginForm, SignUpForm, CreateUserImageForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

def index(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if login_form.is_valid() or signup_form.is_valid():
            # hanle the valid case
            return HttpResponseRedirect(reverse('index'))
    else:
        login_form = LoginForm()
        signup_form = SignUpForm()

    return render(request, 'faceverifier/index.html', {
        'login': login_form,
        'signup': signup_form,
    })


def logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            auth_logout(request)
            return HttpResponseRedirect('./login')

@login_required
def usersetting(request):
    if request.method == 'GET':
        apikey = UserAPIKey.objects.filter(user_id=request.user.id).first()
        if apikey is None:
            key = get_random_string(20)
            apikey = UserAPIKey.objects.create(user_id= request.user , apiKey = key)
        return render(request, 'faceverifier/user/settings.html', {'api_key': apikey})

@login_required
def userlicense(request):
    if request.method == 'GET':
        return render(request, 'faceverifier/user/license.html')


def login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('./home')
            else:
                form.add_error(None, 'Check the email and password')
    else:
        form = LoginForm()

    if request.user.is_authenticated:
        return HttpResponseRedirect('./home')

    return render(request, 'faceverifier/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    # todo: sequence of the form
    return render(request, 'faceverifier/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'faceverifier/user/home.html')

@login_required
def tryapi(request):
    return render(request, 'faceverifier/user/tryapi.html')

@login_required
def uploadimages(request):
    if request.method == 'POST':
        form = CreateUserImageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            # image1 = str(UserImages.objects.last().image)
            # image1 = image1.split("/")
            # image1 = os.path.join(*image1)
            # image1 = os.path.join(MEDIA_ROOT, image1)
            instance.save()
            # em1 = embedder.extract(image1, threshold=0.95)
            # print(em1)
            # if len(em1) > 1:
            #     print("More than one face detected")
            #     more = "More than one face detected"
            #     return render(request, 'faceverifier/user/image.html', {'more_than_one_face_detected': more})
            # elif len(em1) < 1:
            #     print("No face detected")
            #     no = "No face detected"
            #     return render(request, 'basic_app/image.html', {'no_face_detected': no})
            # else:
            #     print("This is done good")
            #     form.save()
            #     img_obj = form.instance
            #     return render(request, 'basic_app/image.html', {'form': form, 'img_obj': img_obj})

    else:
        form = CreateUserImageForm()
    return render(request, 'faceverifier/user/imageUpload.html', {'form': form})


class MultipleFormsDemoView(MultiFormsView):
    template_name = "faceverifier/index.html"
    form_classes = {'login': LoginForm,
                    'signup': SignUpForm,
                    }

    success_urls = {
        'login': reverse_lazy('form-redirect'),
        'signup': reverse_lazy('form-redirect'),
    }

    def login_form_valid(self, form):
        user = UserDetails.objects.filter(email__exact=form.cleaned_data.get('email')).first()
        valid = check_password(form.cleaned_data.get('password'), user.password)
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

    def signup_form_valid(self, form):
        email = form.cleaned_data.get('email')
        form_name = form.cleaned_data.get('action')
        print(email)
        return HttpResponseRedirect(self.get_success_url(form_name))
