from django.conf.urls import url
from . import views
from .models import Board

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<board_info>.+?)/$',views.boardDetails),
    #url(r'^(?P<board_id>[0-9]+)/$',views.boardDetails,name="boardDetails"),
    url(r'^createboard$',views.save_board),
    url(r'^createtask$',views.save_task),
    url(r'^cardsave$',views.save_card),
    url(r'^deleteBoard$', views.deleteBoard),
    url(r'^deleteTask$', views.deleteTask),
    url(r'^deleteCard$',views.deleteCard)

]