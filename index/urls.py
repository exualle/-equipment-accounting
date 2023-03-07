from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import get_items, save, sort, register, rights, index, add, excel_export, remove, get_related_items, sort_rel
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register_view'),
    path('rights', rights),
    path('list', get_items),
    path('save', save),
    path('remove', remove),
    path('add', add),
    path('sorted', sort),
    path('sorted_rel', sort_rel),
    path('related', get_related_items),
    path('range', excel_export),
    path('', index),
]

if(settings.DEBUG):
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
