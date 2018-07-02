from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .models import Book, Author, Publish, gander, AuthorDetial


# Create your views here.

def index(request):
    return render(request, 'index.html')


def addBook(request):
    publish_obj = Publish.objects.all()
    author_obj = Author.objects.all()

    if request.method == 'POST':
        book_name = request.POST.get('name')
        book_price = request.POST.get('price')
        book_author = request.POST.getlist('author_name')
        book_is_pub = request.POST.get('is_pub')
        book_pub_date = request.POST.get('pub_date')
        book_publish_id = request.POST.get('publish_name')

        print(book_author)

        book_obj = Book.objects.create(name=book_name, price=book_price, is_pub=book_is_pub, pub_date=book_pub_date,
                                       publish_id=book_publish_id)

        book_obj.authors.add(*book_author)

        return redirect('/add_book/')

    return render(request, 'addBook.html', {'publish_obj': publish_obj, 'author_obj': author_obj})


def addAuthor(request):
    grand_obj = gander.objects.all()

    if request.method == 'POST':
        author_name = request.POST.get('name')
        author_sex = request.POST.get('grand')
        author_age = request.POST.get('age')
        author_tel = request.POST.get('tel')
        author_email = request.POST.get('email')
        author_address = request.POST.get('address')
        gander_instance = gander.objects.get(id=author_sex)

        author_detial = AuthorDetial.objects.create(email=author_email, address=author_address, tel=author_tel)

        Author.objects.create(name=author_name, age=author_age, sex=gander_instance, authorDetial=author_detial)

        return redirect('/add_author/')

    return render(request, 'addAuthor.html', {'grand_obj': grand_obj})


def addPublish(request):
    if request.method == 'POST':
        publish_name = request.POST.get('name')
        publish_tel = request.POST.get('tel')
        publish_email = request.POST.get('email')
        publish_address = request.POST.get('address')

        Publish.objects.create(name=publish_name, tel=publish_tel, address=publish_address, email=publish_email)

        return redirect('/add_publish/')

    return render(request, 'addPublish.html')


def bookManage(request):
    book_obj = Book.objects.all()

    return render(request, 'bookManage.html', {'book_obj': book_obj})


def compileBook(request, id):
    book_obj = Book.objects.get(id=id)
    publish_obj = Publish.objects.all()
    author_obj = Author.objects.all()

    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_price = request.POST.get('price')
        new_author = request.POST.getlist('author_name')
        new_is_pub = request.POST.get('is_pub')
        new_pub_date = request.POST.get('date')
        new_publish = request.POST.get('publish_name')

        Book.objects.filter(id=id).update(name=new_name, price=new_price, is_pub=new_is_pub,
                                          pub_date=new_pub_date, publish=new_publish)

        book_obj.authors.set(new_author)

        return redirect('/book_manage/')

    return render(request, 'compileBook.html',
                  {'book_obj': book_obj, 'publish_obj': publish_obj, 'author_obj': author_obj})


def delBook(request, id):

    book_obj = Book.objects.get(id=id)
    book_obj.delete()
    # book_obj.authors.remove()

    return redirect('/book_manage/')


def manageAuthor(request):
    author_obj = Author.objects.all()

    return render(request, 'manageAuthor.html', {'author_obj': author_obj})


def managePublish(request):
    publish_obj = Publish.objects.all()

    return render(request, 'managePublish.html', {'publish_obj': publish_obj})


def compileAuthor(request, id):
    author_obj = Author.objects.get(id=id)
    grand_obj = gander.objects.all()
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_grand = request.POST.get('grand')
        new_age = request.POST.get('age')
        new_tel = request.POST.get('tel')
        new_email = request.POST.get('email')
        new_address = request.POST.get('address')

        auth = Author.objects.get(id=id).authorDetial_id

        AuthorDetial.objects.filter(id=auth).update(tel=new_tel, email=new_email, address=new_address)

        Author.objects.filter(id=id).update(name=new_name, age=new_age, sex=new_grand, )
        return redirect('/manage_author/')

    return render(request, 'compileAuthor.html', {'author_obj': author_obj, 'grand_obj': grand_obj})


def delAuthor(request, id):
    author_obj = Author.objects.get(id=id).authorDetial_id
    # Book.authors.remove(Author.objects.get(id=id))
    AuthorDetial.objects.filter(id=author_obj).delete()
    Author.objects.filter(id=id).delete()


    return redirect('/manage_author/')


def compilePublish(request, id):
    publish_obj = Publish.objects.filter(id=id).first()

    if request.method == 'POST':

        new_name = request.POST.get('name')
        new_tel = request.POST.get('tel')
        new_email = request.POST.get('email')
        new_address = request.POST.get('address')

        Publish.objects.filter(id=id).update(name=new_name, tel=new_tel, email=new_email, address=new_address)

        return redirect('/manage_publish/')


    return render(request, 'compilePublish.html', {'publish_obj': publish_obj})


def delPublish(request, id):
    Publish.objects.filter(id=id).delete()

    return redirect('/manage_publish/')
