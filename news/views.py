from django.shortcuts import render
from django.views import generic

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


class NewspaperListView(generic.ListView):
    model = Newspaper
    context_object_name = "manufacturer_list"
    template_name = "news/newspaper_list.html"
    queryset = Newspaper.objects.all()


class TopicListView(generic.ListView):
    model = Topic
    template_name = "news/topic_list.html"


