
from django.conf.urls import include, url,patterns
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
dajaxice_autodiscover()

urlpatterns = patterns("",
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'ecomstore.views.index', name='index'),
    url(r'^test2/', 'ecomstore.view2.index', name='index'),
    url(r'^test3/', 'ecomstore.view3.index', name='index'),
)

from django.conf import settings
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    )

# urlpatterns += staticfiles_urlpatterns()