from rest_framework import routers

from pizza.viewsets import PizzaViewSet, PizzeriaViewSet


router = routers.DefaultRouter()
router.register('pizzas', PizzaViewSet)
router.register('pizzerias', PizzeriaViewSet)
