from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from cliente.ClienteView import Estadisticas,ClienteCrear,ClienteListar



urlpatterns = [
    path('creacliente/', ClienteCrear.as_view(), name='crear'),
    path('listclientes', ClienteListar.as_view(), name='listar'),
    path('kpideclientes', Estadisticas.as_view(), name='estadisticas'),
    
] + static(settings.MEDIA_URL, document_root=settings.DEFAULT_FILE_STORAGE)