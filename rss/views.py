from django.shortcuts import render
from django.http import HttpResponse
import feedparser

# Create your views here.
def index(request):

    #if request.GET.get("url"):
     #   print("REQUEST >>>>", request)
      #  url = request
      #  print("URL >>>> ", url)
      #  feed = feedparser.parse(url)
      #  print("FEED >>>>", feed)
    #else:
        #feed = None
    #return render(request, "rss/reader.html", {"feed": feed})

    if request.GET.get("url"):
        url = request.GET.get("url")
        print("URL >>>> ", url)
        feed = feedparser.parse(url)
        print("FEED >>>>", feed)
    else:
        feed = None

    context = {
        "feed": feed
    }

    return render(request, "rss/reader.html", context)