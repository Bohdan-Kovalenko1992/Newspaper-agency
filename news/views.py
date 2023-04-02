from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import RedactorCreationForm, TopicSearchForm, RedactorUpdateForm

from news.models import Newspaper, Redactor, Topic


def index(request):
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_topics": num_topics,
    }
    return render(request, "news/index.html", context=context)


class RedactorListView(generic.ListView):
    model = Redactor
    queryset = Redactor.objects.all()


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related("newspapers__topics")


class RedactorUpdateView(generic.UpdateView):
    form_class = RedactorUpdateForm
    model = Redactor


class RedactorDeleteView(generic.DetailView):
    model = Redactor
    success_url = reverse_lazy("")


class NewspaperListView(generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "news/newspaper_list.html"
    queryset = Newspaper.objects.all()


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "news/newspaper_detail.html"
    login_url = reverse_lazy("login")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:newspaper-list")


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        context["search_form"] = TopicSearchForm()
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    template_name = "news/topic_form.html"
    success_url = reverse_lazy("news:topic-list")


class TopicDetailView(generic.DetailView):
    model = Topic


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:newspaper-list")

