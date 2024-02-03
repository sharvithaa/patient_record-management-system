from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.signin,name='logout'),
    path('upload',views.image_upload_view,name='upload'),
    path('doctors',views.doctors,name='doctors'),
    path('appointment',views.appointment,name='appointment'),
    path('images',views.image_list,name='image_list'),
    path('delete',views.delete,name='delete')


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)