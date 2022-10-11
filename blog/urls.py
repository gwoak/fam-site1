from django.urls import path
from django.urls import path
from .views import AddPostView, AuthorView, PostView, PostDetailView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    
   path('', PostView.as_view(), name='blog_home'),
   path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'), 
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('add_category/', AddCategoryView.as_view(), name='add_category'),
   path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
   path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
   path('category/<str:cats>', CategoryView, name='category'),
   path('author/<str:author>', AuthorView, name='author')

]