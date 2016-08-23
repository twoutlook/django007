from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
# from django.shortcuts import render

from django.conf import settings
from django.shortcuts import redirect

# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002
from .models import Item003
from .models import Item004 # version 2

# V2
# from .models import Item004v2

from .models import Spec
from .models import Cust

from ipware.ip import get_ip

# def index(request):
#     return HttpResponse("Hello, world. 欠料")
    
    
# def index(request):
#     if not request.user.is_authenticated:
#         # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
#         #return redirect('../admin')
#         context = {'page_title':'xxx','customer_list': {}}
#         return render(request, 'app001/index.html', context)     
        
#     customer_list = Customer.objects.order_by('field1')[:100]
#     context = {'page_title':'yyy','customer_list': customer_list}
#     return render(request, 'app001/index.html', context)     
    
def item000(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'雲端佈告欄','item_list': {}}
        return render(request, 'app001/index.html', context)     
        
    item_list = Item000.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'app001雲端佈告欄','item_list': item_list}
    print("by Mark: to debug here...")
    ip = get_ip(request)
    if ip is not None:
        print("we have an IP address for user: "+ip)
    else:
        print("we don't have an IP address for user")
    return render(request, 'app001/index.html', context)     

def spec(request):
    if not request.user.is_authenticated:
         return redirect('../../admin/login/?next=/app001/spec/')

    item_list = Spec.objects.order_by('field1')[:100]
    context = {'page_title':'App001 SPEC','item_list': item_list,'current_user':request.user}
    return render(request, 'app001/spec.html', context)     

def cust(request):
    # if not request.user.is_authenticated:
    #     # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    #     #return redirect('../admin')
    #     context = {'page_title':'Spec','item_list': {}}
    #     return render(request, 'app001/spec.html', context)     
        
    item_list = Cust.objects.order_by('field1')[:100]
    context = {'page_title':'App001 Cust','item_list': item_list}
    return render(request, 'app001/cust.html', context)     

# def item001obj(request):
#     if not request.user.is_authenticated:
#         context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': {}}
#         return render(request, 'app001/item001.html', context)     
        
#     # item_list = Item001.objects.order_by('field1')[:100]
#     # context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': item_list}
#     context = {'page_title':'item001-obj-富鈦-壓鑄機','item_list': {}}
#     return render(request, 'app001/item001.html', context)     


def item001detail(request, item001_id):
    if not request.user.is_authenticated:
         return redirect('../../admin/login/?next=/app001')
    item001=get_object_or_404(Item001, pk=item001_id)
    context = {'current_user':request.user,'page_title':'item001-富鈦-壓鑄機 編號︰','item001_id': item001_id,'item001': item001,'item001_upper': '/app001/item001/'}
    return render(request, 'app001/item001detail.html', context)     

def item003detail(request, item001_id):
    if not request.user.is_authenticated:
         return redirect('../../admin/login/?next=/app001')
    item001=get_object_or_404(Item003, pk=item001_id)
    context = {'current_user':request.user,'page_title':'item003-富甲-壓鑄機 編號︰','item001_id': item001_id,'item001': item001,'item001_upper': '/app001/item003/'}
    return render(request, 'app001/item001detail.html', context)     


def item001(request):
    # if not request.user.is_authenticated:
    #     context = {'page_title':'item001-富鈦-壓鑄機 編號︰','item_list': {}}
    #     return render(request, 'app001/item001.html', context)     
    if not request.user.is_authenticated:
         return redirect('../../admin/login/?next=/app001')
        
    item_list = Item001.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'item001-富鈦-壓鑄機','item_list': item_list}
    return render(request, 'app001/item001.html', context)     

def item002(request):
    if not request.user.is_authenticated:
        # context = {'page_title':'item002-富鈦-欠料','item_list': {}}
        # return render(request, 'app001/item002.html', context)     
        return redirect('/admin/login/?next=/app001/item002')        
    item_list = Item002.objects.order_by('field1')[:100]
    context = {'current_user':request.user,'page_title':'item002-富鈦-欠料','item_list': item_list}
    return render(request, 'app001/item002.html', context)     


# just use item001.html template
def item003(request):
    if not request.user.is_authenticated:
        context = {'current_user':request.user,'page_title':'item003-富甲-壓鑄機','item_list': {}}
        return render(request, 'app001/item001.html', context)     
        
    item_list = Item003.objects.order_by('field1')[:100]
    context = {'page_title':'item003-富甲-壓鑄機','item_list': item_list}
    return render(request, 'app001/item001.html', context)     




def item004(request):
    if not request.user.is_authenticated:
        context = {'page_title':'item004-富甲-欠料','item_list': {}}
        return render(request, 'app001/item002.html', context)     
        
    item_list = Item004.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'item004-富甲-欠料(版本2)','item_list': item_list}
    return render(request, 'app001/item004.html', context)     

def item004a(request):
    if not request.user.is_authenticated:
        context = {'current_user':request.user,'page_title':'item004-富甲-欠料','item_list': {}}
        return render(request, 'app001/item004a.html', context)     
        
    item_list = Item004.objects.order_by('id')[:400]
    context = {'current_user':request.user,'page_title':'item004-富甲-欠料','item_list': item_list}
    return render(request, 'app001/item004a.html', context)     

# a standard view to logout
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/admin/login/?next=/app001')        
