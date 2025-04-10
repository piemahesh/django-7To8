from django.shortcuts import render,redirect,HttpResponse
from .db import products

# Create your views here.
def getIndexPage(req):
    return render(req, 'index.html')

def addProduct(req):
   if(req.method == 'POST'):
        reqMethod = req.POST
        productName = reqMethod.get("productName")
        price = reqMethod.get("price")
        data = {"productName": productName, "price": price}
        products.insert_one(data)
        return redirect("addProduct")
   else:
       dbProducts = products.find()
       myProduct = []
       for product in dbProducts:
           myProduct.append(product)
       return render(req, 'product.html',{"data":myProduct})
   

def deleteProduct(req):
    print("delete request come")