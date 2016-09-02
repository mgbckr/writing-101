import sys
import urllib.parse
import urllib.request

user = sys.argv[1]
tags = " ".join(sys.argv[2].split(","))
url = "http://www.bibsonomy.org/bib/user/%s/%s?items=999" % (user, urllib.parse.quote(tags))

print("Downloading references from BibSonomy: " + url)
urllib.request.urlretrieve(url, "src/bibliography/bibsonomy.bib")