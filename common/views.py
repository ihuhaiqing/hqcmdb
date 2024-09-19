from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import requests
from django.contrib.auth.models import User
from django.conf import settings

class WeChatLoginView(APIView):
    def post(self, request):
        code = request.data.get('code')
        appid = settings.WX_APPID
        secret = settings.WX_SECRET
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code'
        response = requests.get(url)
        data = response.json()
        openid = data.get('openid')
        # 根据 openid 创建或获取用户
        user, created = User.objects.get_or_create(username=openid)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
