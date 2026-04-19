from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
def index(request):
    now = datetime.now()
    return HttpResponse(f"""
        <h1>Hello from django!!!</h1>
        datetime: {now}
            <ul>
                <li><a href="news/">News</a></li>
                <li><a href="/">Home</a></li>
            </ul>
    """)

class CurrentDateTime(View):
    def get(self, request):
        now = datetime.now()
        return HttpResponse(f"""
                <h1>Hello from django!!!</h1>
                datetime: {now}
            """)


def news(request):

    return HttpResponse(f"""
        <h1>Here some news!</h1>
            <ul>
                <li><a href="news/">News</a></li>
                <li><a href="/">Home</a></li>
            </ul>
    """)