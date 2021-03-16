from django.urls import include, path

from pizza.routers import router as pizza_router

urlpatterns = [
    path('api/', include(pizza_router.urls)),
]
