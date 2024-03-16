
import wikipedia

def scrape(name = "Microsoft", length = 1):
    result = wikipedia.summary("Microsoft",sentences = length)
    return result