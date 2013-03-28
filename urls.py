from django.conf.urls import *
 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^post/tweet_message$', 'messages.views.tweet_post'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#handler500 = 'views.server_error'
#handler404 = 'views.page_404'