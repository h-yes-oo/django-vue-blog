from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post, prev_next_post
from blog.models import Post, Category, Tag


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        # post table 에서 가져온 데이터가 context.object_list 에 들어 있음
        qs = context['object_list']
        # 쿼리셋의 각 오브젝트에 대하여 obj_to_post 로 serialize
        post_list = [obj_to_post(obj, False) for obj in qs]
        # 딕셔너리가 아니므로 safe 는 False 로 설정
        return JsonResponse(data=post_list, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prev_post, next_post = prev_next_post(obj)
        json_data = {
            'post': post,
            'prevPost': prev_post,
            'nextPost': next_post
        }
        return JsonResponse(data=json_data, safe=True, status=200)

class ApiCateTagView(View):
    def get(self, request, *args, **kwargs):
        qs1 = Category.objects.all()
        qs2 = Tag.objects.all()

        cate_list = [cate.name for cate in qs1]
        tag_list = [tag.name for tag in qs2]

        json_data = {
            'cateList': cate_list,
            'tagList': tag_list
        }
        return JsonResponse(data=json_data, safe=True, status=200)
    