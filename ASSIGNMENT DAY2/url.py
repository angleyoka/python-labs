import webbrowser
import random


#function url
def Url():
    pass
    url = ['http://docs.python.org/', 'http://google.com/', 'http://fb.com/',
           'https://twitter.com/', 'https://www.youtube.com/']
    path = url[random.randint(0, 3)] #choose randomly
    return path


path = Url()

print(path)
