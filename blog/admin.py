from django.contrib import admin

from blog.models import Post, Category, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'tag_list', 'title', 'description', 'image', 'create_dt', 'update_dt', 'like')

    # obj 의 의미는 해당 Post 객체
    def tag_list(self, obj):
        return ','.join([t.name for t in obj.tags.all()])

    # 테이블로부터 Post 레코드들을 가져올 때, 관련된 tag 테이블의 레코드들도 함께 가져오도록 하는 것 -> 쿼리 횟수를 줄여 성능 향상 기대
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'short_content', 'create_dt', 'update_dt')
