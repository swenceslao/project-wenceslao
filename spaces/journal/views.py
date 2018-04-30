from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Journal, Dgroup


# JOURNALS
class JournalIndexView(generic.ListView):
	model = Journal
	template_name = 'journal/index.html'
	context_object_name = 'all_journal_entries'

class JournalDetailView(generic.DetailView):
	model = Journal
	template_name = 'journal/detail.html'
	context_object_name = 'journal_entry'

class JournalCreate(CreateView):
	model = Journal
	fields = ['journal_title', 'journal_entry', 'written_by']
	success_url = reverse_lazy('journal:index')

class JournalUpdate(UpdateView):
	model = Journal
	fields = ['journal_title', 'journal_entry']

class JournalDelete(DeleteView):
	model = Journal
	success_url = reverse_lazy('journal:index')

# DGROUP
class DgroupIndexView(generic.ListView):
	model = Dgroup
	template_name = 'dgroup/dgroup.html'
	context_object_name = 'dgroup'

class DgroupDetailView(generic.DetailView):
	model = Dgroup
	template_name = 'dgroup/detail.html'
	context_object_name = 'dgroup'

class DgroupCreate(CreateView):
	model = Dgroup
	fields = ['dgroup_name', 'members']

class DgroupUpdate(UpdateView):
	model = Dgroup
	fields = ['dgroup_name', 'members']

class DgroupDelete(DeleteView):
	model = Journal
	success_url = reverse_lazy('journal:dgroup_index')

# USERS
class UserFormView(View):
	form_class = UserForm
	template_name = 'registration/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			# cleaned (normalized) data below
			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:

				if user.is_active:
					login(request, user)
					# request.user.attribute
					return redirect('journal:index')

		return render(request, self.template_name, {'form': form})