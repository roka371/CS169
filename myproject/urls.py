from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/add$', 'myproject.apps.user.views.add'),
    url(r'^users/login$', 'myproject.apps.user.views.login'),
    url(r'^TESTAPI/resetFixture$', 'myproject.apps.user.views.reset'),
    url(r'^TESTAPI/unitTests$', 'myproject.apps.user.views.test'),
)
