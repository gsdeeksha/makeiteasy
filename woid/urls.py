from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from woid.apps.core import views as core_views
from woid.apps.services import views as services_views
urlpatterns = [
    # path('myproject/',services_views.front_page,name='myproject'),
    path('front_page/', services_views.front_page, name='front_page'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('success/', auth_views.LoginView.as_view(), name='success'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', CreateView.as_view(template_name='registration/signup.html',form_class=UserCreationForm,success_url='/'), name='signup'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),
    path('status/', core_views.status, name='status'),
    path('cookies/', TemplateView.as_view(template_name='core/cookies.html'), name='cookies'),
    path('privacy/', TemplateView.as_view(template_name='core/privacy.html'), name='privacy'),
    path('terms/', TemplateView.as_view(template_name='core/terms.html'), name='terms'),
    path('Ratings/', TemplateView.as_view(template_name='core/Ratings.html'), name='Ratings'),
    path('home/', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('new/', TemplateView.as_view(template_name='core/new.html'), name='new'),
    path('success/', TemplateView.as_view(template_name='core/success.html'), name='success'),
    path('tweet_list/', TemplateView.as_view(template_name='core/tweet_list.html'), name='tweet_list'),
    path('socialmedia/', TemplateView.as_view(template_name='core/socialmedia.html'), name='socialmedia'),
    path('weather/', TemplateView.as_view(template_name='core/weather.html'), name='weather'),
    path('<slug:slug>/', include('woid.apps.services.urls', namespace='services')),

]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        pass

