from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})    
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'
class ItemDelete(DeleteView):
    model = Item
    fields = '__all__'
    success_url = '/'
  

# def item_delete(request, item_description):
#     Item.objects.filter(description=item_description).delete()
#     return redirect('index')