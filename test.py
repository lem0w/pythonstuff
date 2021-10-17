#import google
#import beautifulsoup

#search (query, tld='com', lang='eng', num=10, start=0, stop=None, pause=2.0)
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

#tosearch
query = "kozak development"

for j in search(query, tld="com", num=10, stop=10, pause=2.0):
    print(j)
