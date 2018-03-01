from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from firstapp.models import Webpage, AccessRecord, Topic
from .forms import Webform, AddTopicForm, Userform, UserProfileInfo


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request, 'firstapp/index.html', context=date_dict)


def form_name_view(request):
    form = Webform()

    if request.method == 'POST':
        form = Webform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'firstapp/demoform.html', {'form': form})


def createtopic(request):
    form = AddTopicForm()

    if request.method == 'POST':
        form = AddTopicForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:
            print("error")
    return render(request, 'firstapp/newform.html', {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True

        else:
            print(user_form.errors)


    else:
        user_form = Userform()
        profile_form = UserProfileInfo()
    return render(request, 'firstapp/registeration.html', {'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered
                                                           })

#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponse('User Logout Successfully')
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse('Accounts Not Active')
#         else:
#             return HttpResponse('invaliid login details')
#     else:
#         return render(request, 'firstapp/login.html', {})
