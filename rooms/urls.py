from django.urls import path
from . import views


urlpatterns = [
    path("", views.see_all_rooms),
    # <>안에 입력받을 파라미터의 타입을 적고 :뒤에 원하는 파라미터 명을 적는다. ex) rooms/1 이면 <int:post_id>, rooms/welcome <str:room_name>
    path("<int:room_pk>", views.see_one_room),
]
