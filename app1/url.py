from django.conf.urls import url
from . import views
from app1.view import album, image

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^singin/$', views.singin, name='singin'),
    url(r'^logout/$', views.singout, name='singout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/edit_profile/$', views.UpdateProfile.as_view(), name='update_profile'),
    url(r'user/change_pass/$', views.ChangePass, name='change_pass'),

    # Album
    url(r'^(?P<username>[a-zA-Z0-9]+)/album/create_new/$', album.CreatAlbum.as_view(), name="create_album"),
    url(r'^(?P<username>[a-zA-Z0-9]+)/album/$', album.ViewListAlbum.as_view(), name="list_album"),
    url(r'^detail_album/(?P<pk>[0-9]+)/$', album.DetailAlbum.as_view(), name="detail_album"),

    # Images
    url(r'^images/upload/$', image.UploadImage.as_view(), name="upload_images"),
    url(r'^images/(?P<pk>[0-9]+)/$', image.ViewImage.as_view(), name="detail_image"),
    url(r'^(?P<username>[a-zA-Z0-9]+)/my_photo/$', image.ListImage.as_view(), name="my_image"),
    url(r'^images/like/(?P<pk>[0-9]+)/$', image.LikeImageView.as_view(), name="like_image"),
    url(r'^images/unlike/(?P<pk>[0-9]+)/$', image.UnlikeImageView.as_view(), name="unlike_image"),
    url(r'^images/comment/(?P<pk>[0-9]+)/$', image.CommentImageView.as_view(), name="comment_image"),
]
