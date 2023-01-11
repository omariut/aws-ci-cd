from django.http import HttpResponse

def home(request):
   text = """<h1>Hi! this is our mind blowing home page</h1>"""
   return HttpResponse(text)