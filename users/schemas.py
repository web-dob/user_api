from drf_yasg import openapi


auth_profile_avatar_read = {
    "200": openapi.Response(
        name='Profile',
        in_=openapi.IN_PATH,
        description="Получение аватара профиля",
        examples={
            "application/json": {
                "avatar": "/media/users/admin-%D0%B04_rBb3XWB.jpg"
            }
        },
        type=openapi.TYPE_STRING
    ),
    "404": openapi.Response(
        name='Profile',
        in_=openapi.IN_PATH,
        description="Получение аватара профиля",
        examples={
            "application/json": {
                "error": "Пользователь: admin не имеет профиля"
            }
        },
        type=openapi.TYPE_STRING
    ),
}

auth_profile_avatar_put_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    description="Редактирование аватара профиля",
    properties={
        'avatar': openapi.Schema(type=openapi.TYPE_STRING, example="/media/uploads/user_avatar.jpg"),
    },
)

auth_profile_avatar_put_response = {
    "200": openapi.Response(
        description="Пример ответа при редактировании аватара профиля",
        examples={
            "application/json": {
                "avatar": "/media/uploads/user_avatar.jpg",
            }
        }
    ),
}
