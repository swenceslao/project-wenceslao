from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'journal'

urlpatterns = [
	# register/
	path('register/', views.UserFormView.as_view(), name='register'),
    # login/
    path('login', auth_views.login, name='login'),
    # logout/
    path('logout', auth_views.logout, name='logout'),

    # dgroup/
    path('dgroup', views.DgroupIndexView.as_view(), name='dgroup_index'),
    # dgroup/1
    path('dgroup/<int:pk>', views.DgroupDetailView.as_view(), name='dgroup_detail'),
    # dgroup/create
    path('dgroup/create', views.DgroupCreate.as_view(), name="dgroup_create"),
    # dgroup/1/edit
    path('dgroup/<int:pk>/edit', views.DgroupUpdate.as_view(), name="dgroup_update"),
    # dgroup/1/delete
    path('dgroup/<int:pk>/delete', views.DgroupDelete.as_view(), name="dgroup_delete"),

	# ''
    path('', views.JournalIndexView.as_view(), name='index'),
    # journal/1
    path('journal/<int:pk>', views.JournalDetailView.as_view(), name='journal_detail'),
    # journal/create
    path('journal/create', views.JournalCreate.as_view(), name="journal-write"),
    # journal/1/edit
    path('journal/<int:pk>/edit', views.JournalUpdate.as_view(), name="journal-update"),
    # journal/1/delete
    path('journal/<int:pk>/delete', views.JournalDelete.as_view(), name="journal-delete"),
]