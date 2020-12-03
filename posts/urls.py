from django.urls import path
from . import views as post_views

app_name = "posts"

urlpatterns = [
	path("search/", post_views.SearchFormView.as_view(), name="search"),
]
