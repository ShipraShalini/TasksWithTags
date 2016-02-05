
from django.conf.urls import url, include
from django.views.generic import TemplateView

from src.UI.views.completeformview import complete
from src.UI.views.deleteformview import delete
from src.UI.views.searchformview import search
from src.UI.views.taskformview import task
from src.UI.views.displaytaskview import DisplayTaskView
from src.api.views.modifyview import ModifyView
from src.api.views.showallview import ShowAllView
from src.api.views.taskview import TaskView
from src.api.views.searchview import SearchView

urlpatterns = [
            url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
            url(r'^add/', TaskView.as_view()),
            url(r'^search/', SearchView.as_view()),
            url(r'^modify/', ModifyView.as_view()),
            url(r'^complete-form/', complete),
            url(r'^delete-form/', delete),
            url(r'^task-form/', task),
            url(r'^search-form/', search),
            url(r'^displaytask/', DisplayTaskView.as_view()),
            url(r'^showallview/', ShowAllView.as_view()),

            url(r'^$', TemplateView.as_view(template_name='base.html')),


]

