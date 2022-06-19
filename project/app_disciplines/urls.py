from django.urls import path, include
from app_disciplines import views
from wkhtmltopdf.views import PDFTemplateView


urlpatterns = [
    path('disciplines/', views.dis, name='dis'),
    path('disciplines/ac_conf/', views.academ_conf, name='ac_conf'),
    path('disciplines/reg_list/', views.reg_list, name='reg_list'),
]