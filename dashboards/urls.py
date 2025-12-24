from django.urls import path

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add/',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>/',views.edit_category,name='edit_category'),
]
