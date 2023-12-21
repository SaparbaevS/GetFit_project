from django.views.generic import DetailView

from app.models import Train, TrainCategory, TrainStatus
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'title': 'Get FIt'}
    return render(request, 'app/index.html', context)

@login_required
def train_list(request):
    context = {
        'title': 'Train',
    }

    return render(request, 'app/train.html', context)


def single_train(request, category_id=None):
    if category_id:
        category = TrainCategory.objects.get(id=category_id)
        trains = Train.objects.filter(category=category)
    else:
        trains = Train.objects.all()

    context = {
        'title': 'Single Train',
        'categories': TrainCategory.objects.all(),
        'trains': trains
    }
    return render(request, 'app/single_train.html', context)


class TrainDetailView(DetailView):
    template_name = 'app/detail.html'
    model = Train
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'