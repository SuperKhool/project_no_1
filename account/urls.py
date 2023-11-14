from django.urls import path
from .views import sing_up , sing_in , sing_out

urlpatterns = [
    path('sing_up/',sing_up,name='sing_up'),
    path('sing_in/',sing_in,name='sing_in'),
    path('sing_out/',sing_out,name='sing_out')
]
