from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import ToDoCreateView, ToDoUpdateView, ToDoListView, ToDoDeleteView

# from ../core/views import task_listView, ToDoCreateView, ToDoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task_list/', ToDoListView.as_view(), name='listtodo'),
    path('task_list/add', ToDoCreateView.as_view(), name='addtodo'),
    path('task_list/update/<pk>', ToDoUpdateView.as_view(), name='updatetodo'),
    path('task_list/delete/<pk>', ToDoDeleteView.as_view(), name='deletetodo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
