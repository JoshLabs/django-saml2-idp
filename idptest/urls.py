from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from saml2idp.views import home_page

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^idptest/', include('idptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Required for login:
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='account_login'),

    # URLs for the IDP:
    (r'^idp/', include('saml2idp.urls')),
    url( r'^$', home_page, name="home_page"),
)
