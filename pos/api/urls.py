from django.urls import path, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TablePasienListApiView, TablePasienDetailApiView, TableDokterListApiView, TableDokterDetailApiView, TableAntrianListApiView, TableAntrianDetailApiView, LoginView, LogoutView

app_name = 'api'
urlpatterns = [
    path('api/table_pasien', views.TablePasienListApiView.as_view()),
    path('api/table_pasien/<int:id>', views.TablePasienDetailApiView.as_view()),
    path('api/table_dokter', views.TableDokterListApiView.as_view()),
    path('api/table_dokter/<int:id>', views.TableDokterDetailApiView.as_view()),
    path('api/table_antrian', views.TableAntrianListApiView.as_view()),
    path('api/table_antrian/<int:id>', views.TableAntrianDetailApiView.as_view()),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]