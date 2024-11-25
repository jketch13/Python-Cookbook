import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

long_url = "https://www.example.com/very/long/url"
short_url = shorten_url(long_url)

print("Long URL:", long_url)
print("Short URL:", short_url)