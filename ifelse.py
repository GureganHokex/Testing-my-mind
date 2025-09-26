def normalize_url(url):
    if url.startswith("https://"):
        return url
    elif url.startswith("http://"):
        return "https://" + url[len("http://"):]
    else:
        return "https://" + url