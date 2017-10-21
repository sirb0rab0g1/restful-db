from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
# from .models import Information
from .views import (
    MessagingViewSet,
    MessageSetter,
    PerUserMessage
)

router = DefaultRouter()
router.register(r'message', MessagingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('^messages/(?P<receiver_id>.+)/$', PerUserMessage.as_view()),
    url(r'^msg/$',MessageSetter.as_view(), name='signup'),    # url(r'^upload-profile-image/$',
]
