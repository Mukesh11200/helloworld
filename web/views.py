from django.shortcuts import render,redirect
from .models import note
from .forms import Formaddnote

# Create your views here.
def homepage(request):
    fill = note.objects.all()
    frm = Formaddnote()

    r = Formaddnote(request.POST,request.FILES)

    if r.is_valid():
        temp = r.save()
        temp.save()

    return render(request, 'homepage.html',{'forms':fill,'f':frm})


def delete(request):

    i = request.GET.get('nid')
    o = note.objects.filter(nid=i).delete() 
    return redirect('http://localhost:8000/')




