from rest_framework import routers

from users.viewsets import ManageUserView


router = routers.DefaultRouter()
router.register('users', ManageUserView)
