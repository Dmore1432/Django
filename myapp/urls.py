from django.urls import path,include
from . import views
urlpatterns = [
    path('first/',views.function1),
    path('',views.index),
    path('insertform/',views.Insertform,name='insertform'),
    path('insertdata/',views.Insertdata,name='insertdata'),
    path('showpage/',views.Showpage,name='showpage'),
    path('editpage/<int:pk>',views.Editpage,name='editpage'),
    path('update/<int:pk>',views.Updatedata,name='update'),
    path('delete/<int:pk>',views.Deletedata,name='delete'),
    path('json/',views.json1),
    #class base view route
    # path('jsonCBV/',views.JsonCBV.as_view()),
    # path('parent/',views.parent.as_view()),
    # path('child/',views.child.as_view()),
    # path('just/',views.Just.as_view()),
    # path('register/',views.Registerpage,name='register'),

]