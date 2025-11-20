from django.urls import path
from.import views


urlpatterns = [
    path('',views.Home,name="home"),
    path('create', views.stdForm,name="std"),
    path('regstd/',views.registstd,name="registstd"),
    path('fetch_std',views.retrievestd,name='fetch_std'),
    path('updatestd/<int:pk>',views.updatestd,name='updatestd'),
    path('signup/',views.userRegistration,name="signup"),
    path('login/',views.login_view,name="signin"),
    path('logout/',views.logout,name="signout"),
    path('deletestd/<int:pk>',views.deletestd,name='deletestd')
]
                                                 