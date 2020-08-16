from django.contrib import admin
from django.urls import path,include
from testapp import views
urlpatterns = [
    #pat(h('admin/', admin.site.urls),
    path('',views.todoview,name="show"),
    path('add/',views.addentry,name="addentry"),
    path('del/<int:i>/',views.delentry ,name="delete"),
    path('done/<int:i>/',views.doneview),
    path('fin/<int:i>/',views.finview,name="finished"),
    path('s/',views.showdonee,name='showdone'),
    path('delacc/<int:i>/',views.accdelete,name='delacc'),
    ]
