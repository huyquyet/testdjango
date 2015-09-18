from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.views.generic.detail import SingleObjectMixin
import django


# Create your views here.

class UserObject(SingleObjectMixin):
    model = django.contrib.auth.models.User
    user_kwarg = 'username'

    def get_object(self, queryset=None):
        return self.model.objects.get(
            username=self.kwargs[self.user_kwarg])


def index(request):
    return render(request, 'index.html', {'error': 'loi'})


def login_view(request):
    return render(request, 'user/login.html')


def singin(request):
    # check method request
    # if exists method ==post be submit from " form login "
    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)
        if user_form.is_valid():
            taikhoan = user_form.cleaned_data['username']
            matkhau = user_form.cleaned_data['password']
            user = authenticate(username=taikhoan, password=matkhau)
            # user1  =authenticate()
            if user is not None:
                # check accout is active
                if user.is_active:
                    login(request, user)
                    # return page index
                    return HttpResponseRedirect(reverse('app1:index'))
                else:
                    # login fail return try login
                    return render(request, 'user/login_fail.html', {'error': 'Tai khoan nay ko dc phep dang nhap'})
            else:
                # login fail return try login
                return render(request, 'user/login_fail.html', {'error': 'Nhap tai khoan va mat khau'})
        else:
            return HttpResponseRedirect(reverse('app1:login_view'))
    else:
        return HttpResponseRedirect(reverse('app1:login_view'))


@login_required
def singout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('app1:index'))


def register(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            new_user = user.save()
            return HttpResponseRedirect(reverse('app1:login_view'))
    else:
        user = UserCreationForm()
    return render(request, 'user/register.html', {'form': user})


class UpdateProfile(UserObject, UpdateView):
    fields = ['first_name', 'last_name', 'email']
    template_name = 'user/edit_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateProfile, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('app1:index')

        # def get_object(self, queryset=None):
        #     return self.model.objects.get(username=self.kwargs['username'])


@login_required()
def ChangePass(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app1:login_view'))
    return render(request, 'user/change_pass.html', {'form': form})
