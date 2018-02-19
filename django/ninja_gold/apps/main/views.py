# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render, redirect

# Create your views here.
def index(req):
    if "gold" not in req.session:
        req.session["gold"] = 0
    if "activities" not in req.session:
        req.session["activities"] = ""
    context = {
        "gold": req.session["gold"],
        "activities": req.session["activities"]
    }
    return render(req, 'main/index.html', context)

def process_money(req, building):
    if building == "farm":
        new_gold = random.randint(10, 20)
        req.session["gold"] += new_gold
        req.session["activities"] += "Earned {} gold from the farm!\n".format(new_gold)
    elif building == "cave":
        new_gold = random.randint(5, 10)
        req.session["gold"] += new_gold
        req.session["activities"] += "Earned {} gold from the cave!\n".format(new_gold)
    elif building == "house":
        new_gold = random.randint(2, 5)
        req.session["gold"] += new_gold
        req.session["activities"] += "Earned {} gold from the house!\n".format(new_gold)
    elif building == "casino":
        new_gold = random.randint(-50, 50)
        req.session["gold"] += new_gold
        if int(req.session["gold"]) < 0:
            req.session["gold"] = 0
        if new_gold < 0:
            req.session["activities"] += "Entered a casino and lost {} gold...ouch!\n".format(abs(new_gold))
        else:
            req.session["activities"] += "Entered a casino and won {} gold...yay!\n".format(new_gold)
    return redirect('/')

def clear(req):
    del req.session["gold"]
    del req.session["activities"]
    return redirect('/')
