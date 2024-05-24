from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    # path("",views.index,name="index"),
    # path("<int:ques_id>/",views.detail,name="detail"),
    # path("<int:ques_id>/results/",views.results,name="result"),
    # path("<int:ques_id>/vote/",views.votes,name="vote"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="result"),
    path("<int:ques_id>/vote/", views.votes, name="vote"),
]