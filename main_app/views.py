from django.shortcuts import render, get_object_or_404, redirect
from .models import Test

# Create your views here.

def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def testing(request):
    queryset = Test.objects.get(id=2)
    context = {
        'object_list': queryset
    }
    return render(request, 'tests/test_list.html', context)

def testing_lookup(request, id):
    obj = get_object_or_404(Test, id=id)
    context = {
        'object': obj
    }
    return render(request, 'tests/test_detail.html', context)

def vaccines(request):
    return render(request, 'vaccines.html')

def test_delete(request):
    return render(request, 'tests/test_delete')