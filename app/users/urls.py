from django.urls import include, path

from users.routers import router as user_router

urlpatterns = [
    path('api/', include(user_router.urls)),
]
