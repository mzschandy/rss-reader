from django.shortcuts import render, redirect
from django.http import HttpResponse
import feedparser
from .models import FeedList

# Create your views here.
def index(request):

    feeds = FeedList.objects.all()
    print(feeds)
    for feed in feeds:
        print(feed)
        print(feed.name)
        print(feed.feed)
    
    if request.method == "POST":
        if "feedAdd" in request.POST:
            name = request.POST["name"]
            feedString = request.POST["feed"]
            feed = feedparser.parse(feedString)

            Feed = FeedList(name = name, feed = feed)
            print(Feed)
            #print(Feed.name)
            #print(Feed.feed)
            Feed.save()
            return redirect("/")

     
    context = {
        "feedList": feeds
    }

    
   # if request.GET.get("url"):
   #     url = request.GET.get("url")
   #     print("URL >>>> ", url)
   #     feed = feedparser.parse(url)
   #     print(type(feed))
   #     print("FEED >>>>", feed)
   #     
#
 #   else:
   #     feed = None

   # context = {
   #    "feed": feed
   # }
    
    return render(request, "rss/reader.html", context)