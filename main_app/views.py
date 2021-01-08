from django.shortcuts import render, redirect
from .models import Widget
# from .forms import WidgetForm
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    # widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets})

class WidgetCreate(CreateView):
    model = Widget
    # fields = ['descrpition', 'quantity']
    fields = "__all__"


def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')
