from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from . import models

from .forms import PostSearchForm
from django.db.models import Q

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Post
    paginate_by = 6
    paginate_orphans = 5
    ordering = "pub_date"
    context_object_name = "posts"

class SearchFormView(FormView):
	form_class = PostSearchForm
	template_name = "posts/post_search.html"

	def form_valid(self, form):
		searchWord = form.cleaned_data['search_word']
		post_list = Post.objects.filter(Q(title__icontains = searchWord)).distinct()

		context = {}
		context['form'] = form
		context['search_term'] = searchWord
		context['posts'] = post_list

		return render(
			self.request, 
			self.template_name, 
			context
		)

'''
def search(request):
	posts = models.Post.objects.all()
	q = request.GET['q']
	if q:
		posts = posts.objects.filter(title__icontains=q)
	return render(request, 'posts/post_search.html', {'posts':posts, 'q':q})
'''

