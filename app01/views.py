from django.shortcuts import render,HttpResponse
from app01 import models

def index(request):
    return render(request, "websocket.html")

def getterminal(request):
    return render(request, "dockerTerminal.html")

def test(request):
    return render(request, "test.html")

def add_book(request):
    book = models.Book(id = "0011",title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")

def add_book2(request):
    books = models.Book.objects.create(id="0012",title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    print(books, type(books)) # Book object (18)
    return HttpResponse("<p>数据添加成功！</p>")

def add_book_find(request):
    books = models.Book.objects.all()
    for i in books:
        print(i.title)
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    return HttpResponse("<p>查找成功！</p>")