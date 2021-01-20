# rss-reader
 RSS reader built with Python and Django for CS521 final project

TO INSTALL (Windows)
cd into project folder
1. Run $ python -m venv venv
2. Run $ venv\Scripts\activate.bat
3. Run $ pip install -r requirements.txt
4. Run $ python manage.py runserver
5. Go to localhost:8000

TO INSTALL (Mac/anything that uses native bash)
cd into project folder
1. Run $ python -m venv venv
2. Run $ source venv/bin/activate
3. Run $ pip install -r requirements.txt
4. Run $ python manage.py runserver
5. Go to localhost:8000


***If the command doesn't work, manually install the following packages in step 3:
django
feedparser
django-picklefield


Sample RSS Fields to use
-
Feed Name: NASA Daily Reports
Feed URL: https://blogs.nasa.gov/stationreport/feed/
-
Feed Name: FeedForAll
Feed URL: https://www.feedforall.com/sample-feed.xml
-
Feed Name: BBC
Feed URL: http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml?edition=int
**This is a long feed*
-
Feed Name: Lorem Ipsum
Feed URL: https://lorem-rss.herokuapp.com/feed

