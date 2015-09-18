import os
import shutil
import hashlib
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from app1.models import Images, Comment


class ViewImage(DetailView):
    model = Images
    template_name = 'images/detail_image.html'
    context_object_name = 'images'


class ListImage(ListView):
    model = User
    template_name = 'images/my_photo.html'
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        context = super(ListImage, self).get_context_data(**kwargs)

        context['list_images'] = []
        self.object = self.get_object()
        for alb in self.object.album.all():
            context['list_images'] += alb.images_set.all()
        return context

    def get_object(self, queryset=None):
        return self.model.objects.get(username=self.kwargs['username'])


class UploadImage(CreateView):
    model = Images
    fields = ['name_picture', 'description_picture', 'pic', 'album']
    template_name = 'images/upload_images.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UploadImage, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('app1:detail_album', kwargs={'pk': self.object.album.id})

    def form_valid(self, form):
        # thao tac voi data
        name, ext = os.path.splitext(form.instance.pic.name)
        sha512 = hashlib.sha512()
        name_pic = str((form.instance.pic.name + str(timezone.now())))
        sha512.update(bytes(name_pic))

        filename = sha512.hexdigest()
        form.instance.pic.name = filename + ext
        self.object = form.save()
        return super(UploadImage, self).form_valid(form)


def DeleteImage(request):
    pass


def UpdateImage(request):
    pass


class LikeImageView(UpdateView):
    model = Images
    # context_object_name = 'images'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            self.object.user_like_pic.add(request.user)
            return HttpResponseRedirect(reverse('app1:detail_image', kwargs={'pk': self.object.pk}))
        return HttpResponseForbidden(
            content=b'dang nhap de like anh')

    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class UnlikeImageView(UpdateView):
    model = Images
    # context_object_name = 'images'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            self.object.user_like_pic.remove(request.user)
            return HttpResponseRedirect(reverse('app1:detail_image', kwargs={'pk': self.object.pk}))
        return HttpResponseForbidden(
            content=b'dang nhap de like anh')

    def put(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class CommentImageView(UpdateView):
    model = Comment

    def post(self, request, *args, **kwargs):
        request.u
        if request.user.is_authenticated():
            self.object = self.get_object()
            self.object.user_comment_pic.add(request)