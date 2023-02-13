from django.shortcuts import render,redirect
from numpy import number, product
from django.db.models.aggregates import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import random
# Create your views here.
def indexShop(request):
    data= brandladies.objects.all()
    data1= Brand.objects.all()
    data2= scdb.objects.all()
    return render(request,'index1.html',{'data':data,'data1':data1,'data2':data2})

def regShop(request):
    return render(request,'register1.html')  

def Viewregister(request):
    if request.method=="POST":
        data=Userreg()
        data.username = request.POST.get('username')
        data.password = request.POST.get('password')
        data.comfirm_password = request.POST.get('comfirm_password')
        data.your_email = request.POST.get('your_email')
        data.save()
        return redirect('loginShop')


def loginShop(request):
    return render(request,'login1.html')      

def Viewlogin(request):
    if (request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username=='Admin1' and password=="Admin1"):
            return render(request,'admin/index2admin.html')
        elif (Userreg.objects.filter(username=username,password=password).exists()):
            data = Userreg.objects.filter(username=username,password=password).values('your_email','comfirm_password','id').first()
            request.session['your_email']=data['your_email']
            request.session['comfirm_password']=data['comfirm_password']
            request.session['id']=data['id']
            request.session['username']=username 
            request.session['password']=password
            return redirect('indexShop')
        else:
            return render(request,'login1.html',{'msg':"Sorry... Invalid username or password"})        


def Viewlogout(request):
	del request.session['username']
	del request.session['comfirm_password']
	del request.session['your_email']
	del request.session['password']
	del request.session['id']
	return redirect('loginShop')    

def adminIndexShop(request):
    return render(request,'admin/index2admin.html')    

def review(request):
    return render(request,'review1.html')

def re_view(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        re =request.POST.get('re')
        data = Review(name=name,re=re,email=email)
        data.save()
        return redirect('indexShop')    

def About(request):
    return render(request,'about1.html')  

def ladiesproduct0(request,category):
    if category == "all":
        data = lpro_db.objects.all()
    else:
        data = lpro_db.objects.filter(categorie=category)
    return render(request,'ladiesproduct.html',{'data':data}) 


def ladiessinglepro(request,lid):
    data=lpro_db.objects.filter(id=lid)
    return render(request,'ladiesprosingle.html',{'data':data})


def gentsproduct1(request,categ):
    if categ == "all":
        data1 = Product.objects.all()
    else:
        data1 = Product.objects.filter(pname=categ)
    return render(request,'gentsproduct.html',{'data1':data1}) 

def gentssinglepro(request,gid):
    data1=Product.objects.filter(id=gid)
    return render(request,'gentsprosingle.html',{'data1':data1})     


def kidsproduct2(request,cat):
    if cat == "all":
        data2 = pdb.objects.all()
    else:
        data2 = pdb.objects.filter(category=cat)
    return render(request,'kidsproduct.html',{'data2':data2}) 

def kidssinglepro(request,kid):
    data2=pdb.objects.filter(id=kid)
    return render(request,'kidsprosingle.html',{'data2':data2})  

def Shopcart(request):
    u = request.session.get('id')
    data = shopCart.objects.filter(userid=u,status=0)
    total=shopCart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart1.html',{'data':data,'total':total}) 

def shop_cart(request,kpid):
    if 'id' in request.session:
        total = request.POST.get('total')
        quantity = request.POST.get('quan')
        userid = request.POST.get('id')
        data = shopCart(Kproductid=pdb.objects.get(id=kpid),quantity=quantity,total=total,userid=Userreg.objects.get(id=userid),status=0)
        data.save()
        return redirect('Shopcart')  

@csrf_exempt
def cart_update(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        shopCart.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def Shop_delete(request,did):
    data=shopCart.objects.filter(id=did)
    data.delete()
    return redirect('Shopcart')   


def ShopcartG(request):
    u = request.session.get('id')
    data = shopCart.objects.filter(userid=u,status=0)
    total=shopCart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart2.html',{'data':data,'total':total}) 

def shop_cart_G(request,gpid):
    if 'id' in request.session:
        total = request.POST.get('total')
        quantity = request.POST.get('quan')
        userid = request.POST.get('id')
        data = shopCart(Gproductid=Product.objects.get(id=gpid),quantity=quantity,total=total,userid=Userreg.objects.get(id=userid),status=0)
        data.save()
        return redirect('ShopcartG')  

@csrf_exempt
def cart_update_G(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        shopCart.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def Shop_delete_G(request,Gdid):
    data=shopCart.objects.filter(id=Gdid)
    data.delete()
    return redirect('ShopcartG')   

def ShopcartL(request):
    u = request.session.get('id')
    data = shopCart.objects.filter(userid=u,status=0)
    total=shopCart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart3L.html',{'data':data,'total':total}) 

def shop_cart_L(request,lpid):
    if 'id' in request.session:
        total = request.POST.get('total')
        quantity = request.POST.get('quan')
        userid = request.POST.get('id')
        data = shopCart(Lproductid=lpro_db.objects.get(id=lpid),quantity=quantity,total=total,userid=Userreg.objects.get(id=userid),status=0)
        data.save()
        return redirect('ShopcartL')  

@csrf_exempt
def cart_update_L(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        shopCart.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def Shop_delete_L(request,Ldid):
    data=shopCart.objects.filter(id=Ldid)
    data.delete()
    return redirect('ShopcartL')       

def checkoutp(request):
    u = request.session.get('id')
    data=shopCart.objects.filter(userid=u,status=0)
    count=shopCart.objects.filter(userid=u,status=0).count()
    total=shopCart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'checkoutpage.html',{'data':data,'total':total,'count':count})

def S_check(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        c_name = request.POST.get('c_name')
        post = request.POST.get('post')
        order_place = request.POST.get('order_place')
        u = request.session.get('id')
        order = shopCart.objects.filter(userid=u,status=0)
        for i in order:
            data=ShopCheckout(cartid=shopCart.objects.get(id=i.id),fname=fname,lname=lname,order_place=order_place,c_name=c_name,post=post,number=number,email=email,address1=address1,address2=address2)
            data.save()
            shopCart.objects.filter(id=i.id).update(status=1)
    return redirect('indexShop')  
      

def tchecktable(request):
    data = ShopCheckout.objects.all()
    return render(request,'admin/checktable.html',{'data':data})

def tchecktable1(request):
    data = Review_Analysis.objects.all()
    return render(request,'admin/checktable1.html',{'data':data})

def tchecktable2(request):
    return  render(request,'admin/checktable2.html')

def pma12(request):
    a14="34"
    if(a14==34):
        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))


    if(request.method=="POST"):
        b = request.POST.get('name')
        if(b=="Long Top"):
            a3 =random.randrange(80, 90, 3)

        elif(b=="Jeans"):
            a3 = random.randrange(60,70, 3)

        elif(b=="Short Top"):
            a3 = random.randrange(50,60, 3)
        elif(b=="Shirts"):
            a3 = random.randrange(40,50, 3)
            random.choice(a3)
    return  render(request,'admin/checktable2.html',{'data1':a3})

def check_delete(request,cdid):
    data=ShopCheckout.objects.filter(id=cdid)
    data.delete()
    return redirect('tchecktable') 



def shopcheck(request):
    return render(request,'shopcheckout.html')                
#admin manage

def Bgents(request):
    return render(request,'admin/brandgents.html')

def display_brands(request):
    if request.method=='POST':
        bname=request.POST.get('bname')
        bdes=request.POST.get('bdes')
        img=request.FILES['img']
        data=Brand(bname=bname,bdes=bdes,img=img)
        data.save()
        return redirect('gbtable')

def gbtable(request):
    data = Brand.objects.all()
    return render(request,'admin/gentsBtable.html',{'data':data})

def gbedit(request,bid):
    data = Brand.objects.filter(id=bid)
    return render(request,'admin/editBtable.html',{'data':data})

def gbupdate(request,gbid):
    if request.method=='POST':
        bname=request.POST.get('bname')
        bdes=request.POST.get('bdes')
        try:
            img=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=Brand.objects.get(id=gbid).img
        data=Brand.objects.filter(id=gbid).update(bname=bname,bdes=bdes,img=file)
    return redirect('gbtable')

def gbdelete(request,gbdid):
    data=Brand.objects.filter(id=gbdid).delete()
    return redirect('gbtable') 

#products
def Progents(request):
    data = Product.objects.all()
    data1 = Brand.objects.all()
    return render(request,'admin/progents.html',{'data':data,'data1':data1})

def display_products(request):
    if request.method=='POST':
        pname=request.POST.get('pname')
        brname=request.POST.get('brname')
        pdes=request.POST.get('pdes')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        color=request.POST.get('color')
        size=request.POST.get('size')
        pimg=request.FILES['pimg']
        data=Product(pname=pname,brname=brname,pdes=pdes,price=price,discount=discount,color=color,size=size,pimg=pimg)
        data.save()
    return redirect('gptable')

def gptable(request):
    data = Product.objects.all()
    return render(request,'admin/proGtable.html',{'data':data})

def gpedit(request,pid):
    data = Product.objects.filter(id=pid)
    return render(request,'admin/editGentspro.html',{'data':data})

def gpupdate(request,gpid):
    if request.method=='POST':
        pname=request.POST.get('pname')
        brname=request.POST.get('brname')
        pdes=request.POST.get('pdes')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        color=request.POST.get('color')
        size=request.POST.get('size')
        try:
            pimg=request.FILES['pimg']
            fs = FileSystemStorage() 
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError :
            file=Product.objects.get(id=gpid).pimg
        data=Product.objects.filter(id=gpid).update(pname=pname,brname=brname,pdes=pdes,price=price,discount=discount,color=color,size=size,pimg=file)
    return redirect('gptable')

def gpdelete(request,gpdid):
    data=Product.objects.filter(id=gpdid)
    data.delete()
    return redirect('gptable')
       

#ladies
# 

def Bladies(request):
    return render(request,'admin/brandladies.html')

def addbrands(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        description=request.POST.get('description')
        img=request.FILES['img']
        data=brandladies(fname=fname,description=description,img=img)
        data.save()
        return redirect('LadiesBrandtable') 

def LadiesBrandtable(request):
    data = brandladies.objects.all()
    return render(request,'admin/ladiesBtable.html',{'data':data})  

def Lbrandedit(request,Lid):
    data = brandladies.objects.filter(id=Lid)    
    return render(request,'admin/editLtable.html',{'data':data})       

def Lbrandupdate(request,Luid):
    if request.method == 'POST':  
        fname=request.POST.get('fname')
        description=request.POST.get('description')
        try:
            img=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=brandladies.objects.get(id=Luid).img
        data = brandladies.objects.filter(id=Luid).update(fname=fname,description=description,img=file)
    return redirect('LadiesBrandtable')  

def Lbranddelete(request,Ldid):
    data = brandladies.objects.filter(id=Ldid)
    data.delete()
    return redirect('LadiesBrandtable') 

#ladies pro
def lpro(request):
    pdata=lpro_db.objects.all()
    data2 = brandladies.objects.all()
    return render(request,'admin/proladies.html',{'pdata':pdata,'data2':data2})    

def ladiespro(request):
    if request.method == 'POST':
        product_name=request.POST.get('product_name') 
        categorie=request.POST.get('categorie')
        product_description=request.POST.get('product_description')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        color=request.POST.get('color')
        size=request.POST.get('size')
        img=request.FILES['img']
        pdata=lpro_db(product_name=product_name,categorie=categorie,product_description=product_description,price=price,discount=discount,color=color,size=size,img=img)
        pdata.save()
    return redirect('protable')     

def protable(request):
    pdata=lpro_db.objects.all()
    return render(request,'admin/proLtable.html',{'pdata':pdata})      

def p_edit(request,pe_id):
    pdata=lpro_db.objects.filter(id=pe_id)    
    return render(request,'admin/editLadiespro.html',{'pdata':pdata})

def p_update(request,up):
    if request.method == 'POST':  
        product_name=request.POST.get('product_name') 
        categorie=request.POST.get('categorie')
        product_description=request.POST.get('product_description')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        color=request.POST.get('color')
        size=request.POST.get('size')
        try:
            img=request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=lpro_db.objects.get(id=up).img
        pdata=lpro_db.objects.filter(id=up).update(product_name=product_name,categorie=categorie,product_description=product_description,price=price,discount=discount,color=color,size=size,img=file)
    return redirect('protable')  

def p_delete(request,dd):
    pdata=lpro_db.objects.filter(id=dd).delete()
    return redirect('protable')    

#kids

def kids(request):
    return render(request,'admin/brandkids.html')

def scart(request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        img=request.FILES['img']
        shopcart = scdb (name=name,description=description,img=img)
        shopcart.save()
        return redirect("BKtables")

def BKtables(request):
    shopcart = scdb.objects.all()
    return render(request,'admin/kidsBtable.html',{'shopcart':shopcart})

def edits(request,seid):
    shopcart = scdb.objects.filter(id=seid)
    return render(request,'admin/editKtable.html',{'shopcart':shopcart})

def editsc(request,supid):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage() 
            file = fs.save(img.name, img)
        except MultiValueDictKeyError :
            file=scdb.objects.get(id=supid).img
        shopcart = scdb.objects.filter(id=supid).update(name=name,description=description,img=file)
    return redirect(BKtables)

def kdelete(request,sdid):
    shopcart = scdb.objects.filter(id=sdid)
    shopcart.delete()
    return redirect(BKtables)
#kids pro

def kproduct(request):
    product = scdb.objects.all()
    data = pdb.objects.all()
    return render(request,'admin/prokids.html',{'product':product,'data':data})

def psart(request):
    if request.method == "POST":
        pname=request.POST.get('pname')
        category=request.POST.get('category')
        pdescription=request.POST.get('pdescription')
        color=request.POST.get('color')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        size=request.POST.get('size')
        file2=request.FILES['file2']
        obj=pdb(pname=pname,category=category,pdescription=pdescription,color=color,price=price,discount=discount,size=size,file2=file2)
        obj.save()
        return redirect("ptables")

def ptables(request):
    product=pdb.objects.all()
    return render(request, 'admin/proKtable.html',{'product':product})

def pedits(request,pid):
    product=pdb.objects.filter(id=pid)
    return render(request, 'admin/editKidspro.html',{'product':product})

def peditsc(request,pid):
    if request.method == "POST":
        pname=request.POST.get('pname')
        category=request.POST.get('category')
        pdescription=request.POST.get('pdescription')
        color=request.POST.get('color')
        price=request.POST.get('price')
        discount=request.POST.get('discount')
        size=request.POST.get('size')
        try:
            image_r=request.FILES['image_r']
            fs=FileSystemStorage()
            file=fs.save(image_r.name,image_r)
        except MultiValueDictKeyError:
            file=pdb.objects.get(id=pid).file2
        pdb.objects.filter(id=pid).update(pname=pname,category=category,pdescription=pdescription,color=color,price=price,discount=discount,size=size,file2=file)
    return redirect(ptables)

def pdelete(request,pid):
    pdb.objects.filter(id=pid).delete()
    return redirect(ptables)

def shopkeeper(request):
    return render(request,'sklogin.html')
def shopkeepercheck(request):
    bname = request.POST.get("bname")
    skid = request.POST.get("id")
    if (Brand.objects.filter(bname=bname, id=skid).exists()):
        return render(request, "skhome.html")
    else:
        return HttpResponse("Invalid")
def usertable(request):
    data = Userreg.objects.all()
    return render(request,'admin/usertable.html',{'data':data})




