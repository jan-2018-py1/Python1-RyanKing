from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    return render(req, "main/index.html")

def buy(req):
    if req.POST["product_id"] == '100':
        price = 19.99
    elif req.POST["product_id"] == '101':
        price = 29.99
    elif req.POST["product_id"] == '102':
        price = 5.99
    elif req.POST["product_id"] == '103':
        price = 49.99
    else:
        price = 0
    count = int(req.POST["quantity"])
    req.session["transaction_total"] = count * price
    req.session["count"] += count
    req.session["running_total"] += (count * price)
    return redirect("/checkout")

def checkout(req):
    if "transaction_total" not in req.session:
        req.session["transaction_total"] = 0
    if "count" not in req.session:
        req.session["count"] = 0
    if "running_total" not in req.session:
        req.session["running_total"] = 0
    context = {
        "transaction_total": req.session["transaction_total"],
        "count": req.session["count"],
        "total": req.session["running_total"]
    }
    return render(req, "main/checkout.html", context)

def clear(req):
    del req.session["transaction_total"]
    del req.session["count"]
    del req.session["running_total"]
    return redirect('/checkout')
