from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views as jwt_views
# from .models import Information
from .views import (
    # upload_profile_image,
    # InformationViewSet,
    SignupView,
    UserViewSet
)

router = DefaultRouter()
router.register(r'accounts', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', jwt_views.obtain_jwt_token),
    url(r'^api-token-verify/', jwt_views.verify_jwt_token),
    url(r'^signup/$',SignupView.as_view(), name='signup'),    # url(r'^upload-profile-image/$',
    #   upload_profile_image, name='upload_profile_image'),
]
