import feedparser

# Listing URLs to all feeds
googleai_url = 'http://feeds.feedburner.com/blogspot/gJZg'



googleai_feed = feedparser.parse(googleai_url)

#print (googleai_feed.entries[1].keys())
print (len(googleai_feed.entries))
