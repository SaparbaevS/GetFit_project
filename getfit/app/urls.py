from app.views import index, train_list, single_train, TrainDetailView
from django.urls import path, include

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('train/', train_list, name='train'),
    path('train/single_train/<slug:slug_param>/', TrainDetailView.as_view(), name='detail'),

    path('train/single_train/', single_train, name='single_train'),

    path('train/single_train/category/<int:category_id>/', single_train, name='category'),

    # path('train/single_train/status/<int:status_id>/', single_train, name='status'),

]