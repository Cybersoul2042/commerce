from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random, string

from .models import User, Item, Bid, Comment, Watchlist


def index(request):
    items = Item.objects.all()
    return render(request, "auctions/index.html", {
        "items": items
    })

def Codegenerator():
    codes = []
    for item in Item.objects.all():
        codes.append(item.code)

    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(characters) for i in range(12))
        if(code not in codes):
            return code
        else:
            code = ''.join(random.choice(characters) for i in range(12))

@login_required
def CreateListing(request):
    if request.method == "POST":
        name = request.POST["name"]
        text = request.POST["description"]
        img = request.POST["imageURL"]
        sBid = request.POST["startingBid"]
        category = request.POST["category"]
        code = Codegenerator()
        
        item = Item.objects.create(itemUser = request.user, itemName = f"{name}", itemImage = f"{img}", itemText = f"{text}", itemBid = float(sBid), category = category, watchlisted = False, code = code)
        item.save()
        bid = Bid.objects.create(user = request.user, item = item, bidAmount = sBid)
        bid.save()

        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "auctions/newListing.html")

@csrf_exempt
def ListingPage(request, listingCode):
    item = Item.objects.get(code=f"{listingCode}")
    comments = Comment.objects.filter(item = item)
    if request.user.is_authenticated:
        if request.method == "POST":
            if 'watchlist' in request.POST:
                if item.watchlisted == False:
                    item.watchlisted = True
                    item.save()
                    isWatch = Watchlist.objects.create(user = request.user, item = item)
                    isWatch.save()
            if 'unwatchlist' in request.POST:
                if item.watchlisted == True:
                    item.watchlisted = False
                    item.save()
            if 'bid-submit' in request.POST:
                newBid = request.POST['newBid']
                item.itemBid = float(newBid)
                item.save()
            if 'comment-submit' in request.POST:
                comment = Comment.objects.create(item = Item, user = request.user, comment = request.POST['newComment'])
    else:
        HttpResponseRedirect(reverse("login"))

    return render(request, "auctions/listingpage.html",{
        "item": item
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
