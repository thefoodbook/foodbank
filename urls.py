from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	# url(r'^polls/', include('polls.urls')),
 #    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
