from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('index',index,name='index'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('savetasks',savetasks,name='svaetasks'),
    path('savelist',savelist,name='savelist'),
    path('delete',delete,name='delete'),
    path('display',display,name='display'),
    path('complete',complete,name='complete'),
    path('delTask',delTask,name='delTask'),
    path('delTaskC',delTaskC,name='delTaskC'),
    path('completed',completed,name='completed'),
    path('details',details,name='details'),
    path('logout',logout,name='logout'),
]