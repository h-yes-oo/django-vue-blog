def obj_to_post(obj, flag=True):
    """
    obj 의 각 속성을 serialize 해서, dict 로 변환한다.
    :param obj:
    :param flag: True (모두 보냄, /api/post/99/ 용), False (일부 보냄, /api/post/list/ 용)
    :return:
    """
    # vars 함수의 결과에는 many to many 필드의 속성은 포함되지 않음에 유의할 것
    post = dict(vars(obj))

    if obj.category:
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'

    if obj.tags:
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = 'https://images.squarespace-cdn.com/content/v1/5a43aa577131a554900bb241/1517582374391-EZII4GCD6W5U2SWLMQEB/study-schedule-image_knowledgeovergrades.net.png?format=2500w'

    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'

    # vars 함수의 결과로 포함되는 속성 중 필요 없는 속성 삭제
    del post['_state'], post['category_id'], post['create_dt']

    if not flag:
        del post['tags'], post['update_dt'], post['description'], post['content']

    return post


def prev_next_post(obj):
    try:
        prev_obj = obj.get_previous_by_update_dt()
        prev_dict = {
            'id': prev_obj.id,
            'title': prev_obj.title,
        }
    except obj.DoesNotExist:
        prev_dict = {}

    try:
        next_obj = obj.get_next_by_update_dt()
        next_dict = {
            'id': next_obj.id,
            'title': next_obj.title,
        }
    except obj.DoesNotExist:
        next_dict = {}

    return prev_dict, next_dict

def obj_to_comment(obj):
    comment = dict(vars(obj))

    if obj.update_dt:
        comment['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        comment['update_dt'] = '9999-12-31 00:00:00'

    del comment['_state'], comment['post_id'], comment['create_dt']

    return comment
