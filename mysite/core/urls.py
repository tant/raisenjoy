from django.urls import path
from rest_framework import routers # Dùng router để chạy
from .views import * # Khai dòng này để tham chiếu được các class trong views


router = routers.SimpleRouter() # Chỉ cần dùng simple router là giải quyết hết mấy vấn đề list, insert, update, delete rồi
router.register(r'users', UserViewSet)
router.register(r'races', RaceViewset)
router.register(r'racers', RacerViewset)
router.register(r'bets', BetViewset)


urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += router.urls
