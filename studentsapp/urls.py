from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/', views.register, name='register'),
    path('table/', views.table, name='table'),
    path('feestructure/', views.feestructure, name='feestructure'),
    # path('extra/', views.Register, name='register')
]

'''
def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def table(request):
    return render(request, 'table.html')


def feestructure(request):
    return render(request, 'feestructure.html')


def classfee(request):
    return render(request, 'classfee.html')

'''
