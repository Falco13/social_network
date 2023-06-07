from django.urls import path
from social_network.views import PostList, PostRetrieveDestroy, LikeCreate, DislikeCreate, RegisterView, ProfileUserView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostRetrieveDestroy.as_view()),
    path('posts/<int:pk>/like', LikeCreate.as_view()),
    path('posts/<int:pk>/dislike', DislikeCreate.as_view()),
    path('signup/', RegisterView.as_view()),
    path('profile/', ProfileUserView.as_view()),
]
