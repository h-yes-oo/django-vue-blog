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
        post['image'] = 'https://via.placeholder.com/900x300/'

    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'

    # vars 함수의 결과로 포함되는 속성 중 필요 없는 속성 삭제
    del post['_state'], post['category_id'], post['create_dt']

    if not flag:
        del post['tags'], post['update_dt'], post['description'], post['content']

    return post
