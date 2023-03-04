from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.users.api.views import UserViewSet
from geoapp.api.views import FeatureViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("geoapp", FeatureViewSet)


app_name = "api"
urlpatterns = router.urls
