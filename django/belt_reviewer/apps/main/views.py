from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book, Author, Review
from django.contrib import messages
import bcrypt

def index(req):
    if "id" in req.session:
        return redirect("/books")
    else:
        return render(req, "main/index.html")

def register(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, errors[error])
        return redirect("/")
    else:
        User.objects.create(name=req.POST["name"], alias=req.POST["alias"], email=req.POST["email"], password=bcrypt.hashpw(req.POST["password"].encode(), bcrypt.gensalt()))
        user = User.objects.last()
        req.session["id"] = user.id
        return redirect("/books")

def books(req):
    if "id" not in req.session:
        return redirect("/")
    else:
        user = User.objects.get(id=req.session["id"])
        recent_reviews = Review.objects.all().order_by("-created_at")[:3]
        all_books = Book.objects.all()
        context = {
            "alias": user.alias,
            "recent_reviews": recent_reviews,
            "all_books": all_books
        }
        return render(req, "main/books.html", context)

def display_book(req, num):
    if "id" not in req.session:
        return redirect("/")
    else:
        book = Book.objects.get(id=num)
        user = User.objects.get(id=req.session["id"])
        all_reviews = Review.objects.filter(book=num).order_by("created_at")
        context = {
            "book": book,
            "all_reviews": all_reviews,
            "user_id": user.id
        }
    return render(req, "main/display_book.html", context)

def login(req):
    try:
        user = User.objects.get(email=req.POST["email"])
    except:
        messages.error(req, "Email not found.")
        return redirect ("/")

    if bcrypt.checkpw(req.POST["password"].encode(), user.password.encode()):
        req.session["id"] = user.id
        return redirect("/books")
    else:
        messages.error(req, "Invalid password.")
        return redirect("/")

def logout(req):
    del req.session["id"]
    return redirect("/")

def add(req):
    if "id" not in req.session:
        return redirect("/")
    else:
        all_authors = Author.objects.all().order_by("name")
        context = {"all_authors": all_authors}
        return render(req, "main/add.html", context)

def add_book(req):
    new_book = Book(title=req.POST["title"])
    if len(req.POST["new_author"]) > 0:
        Author.objects.create(name=req.POST["new_author"])
        new_book.author = Author.objects.last()
    else:
        new_book.author = Author.objects.get(id=req.POST["author"])
    new_book.save()
    new_book = Book.objects.last()
    user = User.objects.get(id=req.session["id"])

    new_review = Review.objects.create(content=req.POST["content"], rating=req.POST["rating"], user=user, book=new_book)
    return redirect("/books/{}".format(new_book.id))

def add_review(req):
    user = User.objects.get(id=req.session["id"])
    book = Book.objects.get(id=req.POST["book_id"])
    Review.objects.create(content=req.POST["content"], rating=int(req.POST["rating"]), user=user, book=book)
    return redirect("/books/{}".format(req.POST["book_id"]))

def show_user(req, num):
    if "id" not in req.session:
        return redirect("/")
    else:
        user = User.objects.get(id=num)
        user_reviews = Review.objects.filter(user=user)
        review_count = Review.objects.filter(user=user).count()
        context = {
            "user": user,
            "user_reviews": user_reviews,
            "review_count": review_count
        }
        return render(req, "main/user.html", context)

def delete(req, num):
    review = Review.objects.get(id=num)
    book_id = review.book.id
    review.delete()
    return redirect('/books/{}'.format(book_id))
