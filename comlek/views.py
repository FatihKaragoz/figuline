from django.shortcuts import render
from model.models import newArrivals,products,category,contact,about


def homeview(request):
    product = products.objects.all()
    categories = category.objects.all()
    newArrivalss = newArrivals.objects.all()
    return render(request,'home.html',{"products":product,"newArrivals":newArrivalss,'categories':categories})



def catView(request,cattId="all"):
    product = ""
    categories = category.objects.all()
    if cattId=="all":
        product = products.objects.all()
    else:
        product = products.objects.filter(cat=cattId)
        # product = products.objects.all()
        return render(request, 'product.html', {'products':product,'control':'all','categories':categories,'category':cattId})
    return render(request,'product.html',{'products':product,'categories':categories,'control':'all'})


def proView(request,proId="all"):
    product = products.objects.filter(pro_id=proId)
    if proId!="all":
        return render(request, 'product.html',{'product':product,'control':'1'})


def contactview(request):
    contactmodel = contact.objects.all()
    return render(request,'contact.html',{'contact':contactmodel})

def aboutview(request):
    aboutModel = about.objects.all()
    return render(request,'about.html',{'about':aboutModel})