from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Test

#Our class based views are here now:

class TestsListView(View):
    def get(self, request):
        queryset = Test.objects.all()
        context = {
            'object_list': queryset
        }
        return render(request, 'tests/test_list.html', context)
        
# Create your views here.

def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def testing_lookup(request, id):
    obj = get_object_or_404(Test, id=id)
    context = {
        'object': obj
    }
    return render(request, 'tests/test_detail.html', context)

def vaccines(request):
    return render(request, 'vaccines.html')

def test_delete(request, id):
    obj = get_object_or_404(Test, id=id)
    if request.method == "POST":
        #Confirming my delete so they don't accidentally delete it
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, 'tests/test_delete.html', context)