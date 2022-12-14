from django.urls import path

from .views import (dashboard, enrollnow, generate_auth_token, index, loginuser,
                    signinuser, signup, signupuser,logoutuser)

urlpatterns = [
    path('signup/', signup, name='signup'), #API
    path('login/', loginuser, name='login'), #API
    path('generate-auth-token/', generate_auth_token, name='generate-auth-token'), #API

    path('dashboard',dashboard,name='dashboard'), #webpoint
    path('',index,name='index'), #home webpoint
    path('signinuser/',signinuser,name='userlogin'),
    path('signupuser/',signupuser,name='signupuser'),
    path('enrollnow/',enrollnow,name ="enroll"),
    path('logout',logoutuser,name='logout')
]