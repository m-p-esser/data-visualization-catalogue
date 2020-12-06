from django.shortcuts import render
from dataviz_gallery.models import Plot

# Create your views here.


def hello_world(request):
    return render(request, 'hello_world.html', {})


def plot_index(request):
    plot_types = Plot.objects.all()
    context = {
        'plot_types': plot_types,
    }
    return render(request, 'plot_index.html', context)


def plot_detail(request, pk):
    plot_type = Plot.objects.get(pk=pk)
    context = {
        'plot_type': plot_type
    }
    return render(request, 'plot_detail.html', context)
