from django.urls import path
from . import views

app_name='forums'

urlpatterns = [
    path('forums/<int:forum_id>',views.forum,name='forum'),
]