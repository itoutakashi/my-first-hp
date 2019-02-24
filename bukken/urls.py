from django.urls import path
from . import views

urlpatterns=[
    path('',views.bukken_itiran,name='bukken_itiran'),
    path('bukken_kensaku/',views.bukken_kensaku,name='bukken_kensaku'),
    path('bukken_kensaku_area/',views.bukken_kensaku_area,name='bukken_kensaku_area'),
    path('bukken_kensaku_area_kensaku/',views.bukken_kensaku_area_kensaku,name='bukken_kensaku_area_kensaku'),
    path('bukken_kensaku_area_outof23/',views.bukken_kensaku_area_outof23,name='bukken_kensaku_area_outof23'),
    path('bukken_kensaku_area_outof23_kensaku/',views.bukken_kensaku_area_outof23_kensaku,name='bukken_kensaku_area_outof23_kensaku'),
    path('bukken_kensaku_area_oot/',views.bukken_kensaku_area_oot,name='bukken_kensaku_area_oot'),
    path('bukken_kensaku_area_oot_kensaku/',views.bukken_kensaku_area_oot_kensaku,name='bukken_kensaku_area_oot_kensaku'),
    path('bukken_syousai/<int:id>/',views.bukken_syousai,name='bukken_syousai'),
]