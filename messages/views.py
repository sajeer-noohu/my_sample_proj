from django.shortcuts import render_to_response
from django.template import RequestContext 
from messages.forms import TweetForm 
from django.http import HttpResponse
from messages.utils import validate_tweet_message



def tweet_post(request):
    # Create your views here.
    
    if request.POST:
        form = TweetForm(data=request.POST)
        if form.is_valid():
            from messages.models import Tweet
            tweet = Tweet()
            tweet.original_tweet_message = request.POST.get('tweet_message')
            tweet.save()
            return HttpResponse('Saved twet')
    else:    
        form = TweetForm(data=None)
        d = {
             'form': form,
             }
        return render_to_response('messages/add_tweet.html', d, context_instance=RequestContext(request))