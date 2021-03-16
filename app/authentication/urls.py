from django.urls import path, include

from authentication import views


urlpatterns = [

    path('token/',
         views.CreateTokenView.as_view(),
         name='token'
    ),

    path(
        'reset_password/',
        include('django_rest_passwordreset.urls',
                namespace='password_reset')
    )

]
