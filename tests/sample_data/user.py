class User:
    """
    样例数据
    """
    def __init__(self, user_info: dict):
        for key, value in user_info.items():
            setattr(self, key, value)


common_user_1 = User(
    user_info={
        "id": 1,
        "nickname": "test nickname",
        "is_admin": False,
        "is_staff": False,
        "is_ta": False,
        "is_ta_admin": False,
        "is_teacher": False,
        "is_editor": False,
        "is_tutor": False,
        "is_superuser": False,
        "avatar": "test_avatar_1",
        "subscribed": False,
        "email": "test_1@ninechapter.com",
        "country_code": "86",
        "phone_number": "123456",
        "is_paid": False,
        "full_name": "test_full_name_1",
        "refer_code": '123',
        "tags": ("test_1", "test_2"),
        "is_completed": False,
        "is_activated": True,
        "is_authenticated": True,
        "lintcode_id": "1",
        "lintcode_data": {},
        "timezone": 1,
        "has_bind_wechat": False,
        "has_bind_wechat_oa": False,
        "credit": 1,
    }

)


common_user_2 = User(
    user_info={
        "id": 2,
        "nickname": "test nickname 2",
        "is_admin": False,
        "is_staff": False,
        "is_ta": False,
        "is_ta_admin": False,
        "is_teacher": False,
        "is_editor": False,
        "is_tutor": False,
        "is_superuser": False,
        "avatar": "test_avatar_2",
        "subscribed": False,
        "email": "test_2@ninechapter.com",
        "country_code": "86",
        "phone_number": "12345672",
        "is_paid": False,
        "full_name": "test_full_name_2",
        "refer_code": '1243',
        "tags": ("test_12", "test_22"),
        "is_completed": False,
        "is_activated": True,
        "is_authenticated": True,
        "lintcode_id": "2",
        "lintcode_data": {},
        "timezone": 2,
        "has_bind_wechat": True,
        "has_bind_wechat_oa": False,
        "credit": 2,
    }
)
