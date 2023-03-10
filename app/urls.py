from django.contrib import admin
from django.urls import path, include, re_path
from app.views import Sum, HistoryViewSet, TotalViewSet

urlpatterns = [
    path('sum/<int:a>&<int:b>', Sum.as_view()),
    path('history/', HistoryViewSet.as_view({'get': 'list'})),
    path('total/', TotalViewSet.as_view()),
]