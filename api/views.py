from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post, prev_next_post
from blog.models import Post, Category, Tag


class ApiPostLV(BaseListView):
    # get_queryset 을 오버라이딩하는 경우 아래 줄이 필요 없음
    # model = Post
    def get_queryset(self):
        # 장고에서 쿼리스트링을 파싱하는 방식
        param_cate = self.request.GET.get('category')
        param_tag = self.request.GET.get('tag')
        if param_cate:
            qs = Post.objects.filter(category__name__iexact=param_cate)
        elif param_tag:
            qs = Post.objects.filter(tags__name__iexact=param_tag)
        else:
            qs = Post.objects.all()
        return qs

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
