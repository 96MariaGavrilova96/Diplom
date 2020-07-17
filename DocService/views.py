import csv

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from DocService.forms import DocForm
from DocService.models import Document


@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/registrationBook")
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, "DocService/signinPage.html", args)
    else:
        return render(request, "DocService/signinPage.html", args)


def logout(request):
    auth.logout(request)
    return redirect("/")


@csrf_protect
def registrationBook(request):
    args = {}
    user = auth.get_user(request)
    args['username'] = user
    if request.POST:
        arg1 = request.POST.get('arg1')
        arg2 = request.POST.get('arg2')
        arg3 = request.POST.get('arg3')
        arg4 = request.POST.get('arg4')
        arg5 = request.POST.get('arg5')
        arg6 = request.POST.get('arg6')
        arg7 = request.POST.get('arg7')
        arg8 = request.POST.get('arg8')
        arg9 = request.POST.get('arg9')
        docForm = Document.objects.all()
        if arg1 != "":
            docForm.filter(reg_number=arg1)
        if arg2 != "":
            docForm.filter(track_number__contains=arg2)
        if arg3 != "":
            docForm.filter(get_date__contains=arg3)
        if arg4 != "":
            docForm.filter(regist_date__contains=arg4)
        if arg5 != "":
            docForm.filter(get_type__contains=arg5)
        if arg6 != "":
            docForm.filter(doc_type__contains=arg6)
        if arg7 != "":
            docForm.filter(from_person__contains=arg7)
        if arg8 != "":
            docForm.filter(description__contains=arg8)
        if arg9 != "":
            docForm.filter(to_person__contains=arg9)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(
            ['Вх. №', 'Трек №', 'Дата получения', 'Дата регистрации', 'Способ получения',
             'Тип документа', 'Контрагент',
             'Содержание', 'Адресат', 'Комментарий'])
        for val in docForm:
            writer.writerow(
                [val.reg_number, val.track_number, val.get_date, val.regist_date, val.get_type, val.doc_type,
                 val.from_person, val.description, val.to_person, val.comment])

        return response
    else:
        docForm = Document.objects.all().filter(reg_person=user.username) | Document.objects.all().filter(
            to_person=user.username)
        return render(request, "DocService/registrationBookPage.html", {'args': args, 'docForm': docForm})


@csrf_protect
def addDocument(request):
    args = {}
    user = auth.get_user(request)
    args['username'] = user
    docForm = DocForm
    if request.POST:
        docForm = DocForm(request.POST)
        if docForm.is_valid():
            doc = docForm.save(commit=False)
            doc.reg_person = user.username
            docForm.save()
            return redirect("readDocument", docForm.instance.reg_number)
        else:
            return render(request, "DocService/addNewDoc.html", {'docForm': docForm, 'args': args})
    else:
        return render(request, "DocService/addNewDoc.html", {'docForm': docForm, 'args': args})


def readDocument(request, number):
    args = {}
    user = auth.get_user(request)
    args['username'] = user
    docForm = Document.objects.get(reg_number=number)
    return render(request, "DocService/readonlyDoc.html", {'args': args, 'docForm': docForm})


def editDocument(request, number):
    args = {}
    user = auth.get_user(request)
    args['username'] = user
    docForm = Document.objects.get(reg_number=number)
    if request.POST:
        docForm.from_person = request.POST.get('from_person')
        docForm.description = request.POST.get('description')
        docForm.get_date = request.POST.get('get_date')
        docForm.to_person = request.POST.get('to_person')
        docForm.get_type = request.POST.get('get_type')
        docForm.doc_type = request.POST.get('doc_type')
        docForm.track_number = request.POST.get('track_number')
        docForm.comment = request.POST.get('comment')
        docForm.save()
        return redirect("readDocument", number)
    else:
        return render(request, "DocService/editDoc.html", {'args': args, 'docForm': docForm})


def removeDocumment(request, number):
    Document.objects.get(reg_number=number).delete()
    return redirect("/registrationBook")


def csvView(request, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response
