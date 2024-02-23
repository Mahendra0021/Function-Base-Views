
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.add_show,name='Home'),
    path('Update/<int:id>/',views.update,name='update'),
    path('Delete/<int:id>/',views.delete,name='delete'),

]

