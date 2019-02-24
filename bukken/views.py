from django.shortcuts import render
from django.http import HttpResponse
from .models import Bukken_Itiran
from .forms import KensakuForm
from django.db.models import Q

def bukken_itiran(request):
    form = KensakuForm()
    bukken_itiran_db = Bukken_Itiran.objects.order_by('公開日')
    return render(request,'bukken/bukken_itiran.html',{'bukken_itiran_db':bukken_itiran_db,'form':form,},)

def bukken_kensaku(request):
    form = KensakuForm(request.POST)
    str = request.POST['find']
    bukken_kensaku_db = Bukken_Itiran.objects.filter(Q(タイトル__contains=str)|Q(住所__contains=str)|Q(地名_俗名__contains=str)|Q(間取り__contains=str)|Q(紹介文__contains=str))
    return render(request,'bukken/bukken_kensaku.html',{'bukken_kensaku_db':bukken_kensaku_db,'form':form,},)

#------------------------------------------------------------------------------
def bukken_kensaku_area(request):
    form = KensakuForm()
    東京２３区 = ["足立区","荒川区","板橋区","江戸川区","大田区","葛飾区","北区","江東区","品川区","渋谷区","新宿区","杉並区","墨田区","世田谷区","台東区","千代田区","中央区","豊島区","中野区","練馬区","文京区","港区","目黒区"]
    bukken_kensaku_area_db = Bukken_Itiran.objects.filter(都道府県__contains='東京',市区町村__in=東京２３区)
    return render(request,'bukken/bukken_kensaku_area.html',{'bukken_kensaku_area_db':bukken_kensaku_area_db,'form':form,},)

def bukken_kensaku_area_kensaku(request):
    form = KensakuForm(request.POST)
    str = request.POST['find']
    東京２３区 = ["足立区","荒川区","板橋区","江戸川区","大田区","葛飾区","北区","江東区","品川区","渋谷区","新宿区","杉並区","墨田区","世田谷区","台東区","千代田区","中央区","豊島区","中野区","練馬区","文京区","港区","目黒区"]
    bukken_kensaku_area_db = Bukken_Itiran.objects.filter(都道府県__contains='東京',市区町村__in=東京２３区)
    bukken_kensaku_area_kensaku_db = bukken_kensaku_area_db.filter(Q(タイトル__contains=str)|Q(住所__contains=str)|Q(地名_俗名__contains=str)|Q(間取り__contains=str)|Q(紹介文__contains=str))
    return render(request,'bukken/bukken_kensaku_area_kensaku.html',{'bukken_kensaku_area_kensaku_db':bukken_kensaku_area_kensaku_db,'form':form,},)
#------------------------------------------------------------------------------
def bukken_kensaku_area_outof23(request):
    form = KensakuForm()
    東京２３区 = ["足立区","荒川区","板橋区","江戸川区","大田区","葛飾区","北区","江東区","品川区","渋谷区","新宿区","杉並区","墨田区","世田谷区","台東区","千代田区","中央区","豊島区","中野区","練馬区","文京区","港区","目黒区"]
    bukken_itiran = Bukken_Itiran.objects.all()
    list_x = []
    for i in bukken_itiran:
        y = i.市区町村
        list_x.append(y)
    set_ab=set(list_x)-set(東京２３区)
    list_ab=list(set_ab)
    bukken_kensaku_area_outof23_db = Bukken_Itiran.objects.filter(都道府県__contains='東京',市区町村__in=list_ab)
    return render(request,'bukken/bukken_kensaku_area_outof23.html',{'bukken_kensaku_area_outof23_db':bukken_kensaku_area_outof23_db,'form':form,},)

def bukken_kensaku_area_outof23_kensaku(request):
    form = KensakuForm(request.POST)
    str = request.POST['find']
    東京２３区 = ["足立区","荒川区","板橋区","江戸川区","大田区","葛飾区","北区","江東区","品川区","渋谷区","新宿区","杉並区","墨田区","世田谷区","台東区","千代田区","中央区","豊島区","中野区","練馬区","文京区","港区","目黒区"]
    bukken_itiran = Bukken_Itiran.objects.all()
    list_x = []
    for i in bukken_itiran:
        y = i.市区町村
        list_x.append(y)
    set_ab=set(list_x)-set(東京２３区)
    list_ab=list(set_ab)
    bukken_kensaku_area_outof23_db = Bukken_Itiran.objects.filter(都道府県__contains='東京',市区町村__in=list_ab)
    bukken_kensaku_area_outof23_kensaku_db = bukken_kensaku_area_outof23_db.filter(Q(タイトル__contains=str)|Q(住所__contains=str)|Q(地名_俗名__contains=str)|Q(間取り__contains=str)|Q(紹介文__contains=str))
    return render(request,'bukken/bukken_kensaku_area_outof23_kensaku.html',{'bukken_kensaku_area_outof23_kensaku_db':bukken_kensaku_area_outof23_kensaku_db,'form':form,},)
#------------------------------------------------------------------------------
def bukken_kensaku_area_oot(request):
    form = KensakuForm()
    tokyo = ['東京都']
    bukken_itiran = Bukken_Itiran.objects.all()
    list_x=[]
    for i in bukken_itiran:
        y = i.都道府県
        list_x.append(y)
    set_ab=set(list_x)-set(tokyo)
    list_ab=list(set_ab)
    bukken_kensaku_area_oot_db = Bukken_Itiran.objects.filter(都道府県__in=list_ab)
    return render(request,'bukken/bukken_kensaku_area_oot.html',{'bukken_kensaku_area_oot_db':bukken_kensaku_area_oot_db,'form':form,},)

def bukken_kensaku_area_oot_kensaku(request):
    form = KensakuForm(request.POST)
    str = request.POST['find']
    tokyo = ['東京都']
    bukken_itiran = Bukken_Itiran.objects.all()
    list_x=[]
    for i in bukken_itiran:
        y = i.都道府県
        list_x.append(y)
    set_ab=set(list_x)-set(tokyo)
    list_ab=list(set_ab)
    bukken_kensaku_area_oot_db = Bukken_Itiran.objects.filter(都道府県__in=list_ab)
    bukken_kensaku_area_oot_kensaku_db = bukken_kensaku_area_oot_db.filter(Q(タイトル__contains=str)|Q(住所__contains=str)|Q(地名_俗名__contains=str)|Q(間取り__contains=str)|Q(紹介文__contains=str))
    return render(request,'bukken/bukken_kensaku_area_oot_kensaku.html',{'bukken_kensaku_area_oot_kensaku_db':bukken_kensaku_area_oot_kensaku_db,'form':form,},)
#------------------------------------------------------------------------------
def bukken_syousai(request,id):
    bukken_syousai_db = Bukken_Itiran.objects.all()[int(id-1):int(id)]
    return render(request,'bukken/bukken_syousai.html',{'bukken_syousai_db':bukken_syousai_db},)
