from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post
from blog.models import Post


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        # post table 에서 가져온 데이터가 context.object_list 에 들어 있음
        qs = context['object_list']
        # 쿼리셋의 각 오브젝트에 대하여 obj_to_post 로 serialize
        postList = [obj_to_post(obj, False) for obj in qs]
        # 딕셔너리가 아니므로 safe 는 False 로 설정
        return JsonResponse(data=postList, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        return JsonResponse(data=post, safe=True, status=200)