from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from app1.models import Album, Images
from django.contrib.auth.models import User
from select import select


class ViewListAlbum(DetailView):
    model = User
    context_object_name = 'anuser'
    template_name = 'album/list_album.html'

    def get_context_data(self, **kwargs):
        context = super(ViewListAlbum, self).get_context_data(**kwargs)
        context['list_album'] = self.object.album.all()
        return context

    def get_object(self, queryset=None):
        return self.model.objects.get(username=self.kwargs['username'])
        # default get_object argument ( queryset, pk anh slug )
        # if you want change arguments, you need overwrite it


class CreatAlbum(CreateView):
    model = Album
    fields = ['name_album', 'description_album']
    template_name = 'album/create_album.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CreatAlbum, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_creat_album = self.request.user
        # self.object = \
        form.save()
        return super(CreatAlbum, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('app1:list_album', kwargs={'username': self.request.user})

    def DeleteAlbum(request):
        pass

    def UpdateAlbum(request):
        pass


class DetailAlbum(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'album/detail_album.html'

    def get_context_data(self, **kwargs):
        context = super(DetailAlbum, self).get_context_data(**kwargs)
        context['list_images'] = self.object.images_set.all()
        return context
