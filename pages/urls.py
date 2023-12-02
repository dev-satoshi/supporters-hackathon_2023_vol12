from django.urls import include, path
from rest_framework.routers import DefaultRouter

# viewのクラスをインポート
from .views import PostViewSet  # ビューセットをインポート
from .views import AboutPageView, HomePageView, PostCreateView, PostFeedView

# ルータを作成
router = DefaultRouter()

# ルーターにビューセットを登録
router.register(r"post", PostViewSet)

from .views import AboutPageView, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post_create/", PostCreateView.as_view(), name="post_create"),
    path("post_feed", PostFeedView.as_view(), name="post_feed"),
    path("", include(router.urls)),  # APIのルート
]
