from django.contrib import admin
from django.urls import include, path

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # главная страница
    path('', include ('core.urls')),
    # товары
    path('items/', include ('item.urls')),
    # страница пользователя
    path('dashboard/', include ('dashboard.urls')),
    # взаимодействие с пользователями
    path('inbox/', include ('conversation.urls')),
    # админка
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
