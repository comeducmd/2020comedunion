from django.shortcuts import render
from django.views.generic import ListView

# from django.views.generic.edit import FormView
from . import models

# from .forms import PostSearchForm
from django.db.models import Q

# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Post
    paginate_by = 6
    paginate_orphans = 0
    ordering = "pub_date"
    context_object_name = "posts"

    def get_queryset(self):
        posts = models.Post.objects.all()
        q = self.request.GET.get("search_word", "")
        if q:
            posts = posts.filter(title__icontains=q)
        return posts


"""
def search(request):
	posts = models.Post.objects.all()
	q = request.GET.get('search_word', '')
	if q:
		posts = posts.filter(title__icontains=q)
	return render(request, 'posts/post_search.html', {'posts':posts, 'q':q})


class SearchFormView(FormView):
	form_class = PostSearchForm
	template_name = "posts/post_search.html"

	def form_valid(self, form):
		print('*')
		searchWord = form.cleaned_data['search_word']#form.cleaned_data['search_word']
		post_list = Post.objects.filter(
				Q(title__icontains = searchWord) | Q(description__icontains=searchWord)
			).distinct()

		context = {}
		context['form'] = form
		context['search_word'] = searchWord
		context['posts'] = post_list
		return render(self.request, self.template_name, context)

	def get_queryset(self):
		print('*')
		query = self.request.GET.get('search_word')
		if query:
			posts = models.Post.objects.filter(title__icontains=query)
		else:
			posts = models.Post.objects.none()
		return posts
"""
