from django.shortcuts import render,redirect,HttpResponse
from .db import products
from bson import ObjectId

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
           product["docId"] = str(product["_id"])
           myProduct.append(product)
       print(myProduct)
       return render(req, 'product.html',{"data":myProduct})
   

def deleteProduct(req,id):
    products.delete_one({'_id':ObjectId(id)})
    return redirect("addProduct")
    
def editProduct(req,id):
    if(req.method == 'GET'):
        product = products.find_one({'_id':ObjectId(id)})
        product['docId'] = str(product['_id'])
        print("======================================================================")
        print(product)
        print("======================================================================")
        return render(req,"edit.html",{"data":product})
    elif(req.method == "POST"):
        print(id)
        reqMethod = req.POST
        productName = reqMethod.get("productName")
        price = reqMethod.get("price")
        data = {"productName": productName, "price": price}
        products.update_one({'_id':ObjectId(id)},{"$set":data})
        print(data,"[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]")
        return redirect("addProduct")
        # products.insert_one(data)