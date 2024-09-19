from django.urls import path

from common.views import WeChatLoginView

urlpatterns = [
    path('token', WeChatLoginView.as_view(), name='wechat_login'),
]
