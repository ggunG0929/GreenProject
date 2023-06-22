from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='community'),                            # post 리스트
    path('<int:post_id>/', views.detail, name='detail'),                    # post_id로 상세보기
    path('write/', views.post_create, name='post_create'),                  # post 작성
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),   # post_id로 삭제
]
