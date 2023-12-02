from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet  # ビューセットをインポート


# viewのクラスをインポート
from .views import HomePageView, AboutPageView, PostCreateView, PostFeedView

# ルータを作成
router = DefaultRouter()

# ルーターにビューセットを登録
router.register(r"post", PostViewSet)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("post_feed", PostFeedView.as_view() ,name="post_feed"),
    path('', include(router.urls))  # APIのルート
]
