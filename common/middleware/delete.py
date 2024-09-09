import re
from django.utils.deprecation import MiddlewareMixin

class DeleteOperationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 使用正则表达式匹配后台删除操作的 URL
        delete_pattern = re.compile(r'/.*/delete/')
        request.is_delete_operation = bool(delete_pattern.search(request.path)) or request.method == 'POST'
