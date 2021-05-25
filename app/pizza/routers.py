from rest_framework import routers

from pizza.viewsets import ManagePizzaView, ManagePizzeriaView


router = routers.DefaultRouter()
router.register('pizzas', ManagePizzaView)
router.register('pizzerias', ManagePizzeriaView)
