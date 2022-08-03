from django.contrib import admin
from django.urls import path, include, re_path
import os
from django.views.static import serve
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# from django.conf.urls import url

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

# add path to all webapp in main path of project
urlpatterns = [
    path("ads/", include("ads.urls")),
    path("cats/", include("cats.urls")),
    path("autos/", include("autos.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("hello/", include("hello.urls")),
    path("", TemplateView.as_view(template_name="home/main.html")),
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")),
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')