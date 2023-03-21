from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import *

import wikipedia

def index(request):
    if request.method == "GET":
        search = request.GET.get("search")
        if search is not None:
            try:
                found = True
                relevant_page = wikipedia.page(search)
                title = relevant_page.original_title
                content = relevant_page.summary
                context = {"title": title, "content": content, "found":found}
            except wikipedia.DisambiguationError as e:
                found = False
                s = e.options
                context = {"arr": s, "found":found}
            return render(request, "parser/index.html", context)
    return render(request, "parser/index.html")

def add(request, title, content):
    if request.method == "POST":
        f = Post(title = title, content = content)
        if Post.objects.filter(title = title).exists(): 
            messages.error(request, "This post already exists in database")
        else:
            messages.success(request, "This post was succesfully added to a database!")
        f.save()
        return HttpResponseRedirect(reverse("parser:index"))