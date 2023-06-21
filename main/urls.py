from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views.homepage import home, aboutus, FullView
from .views.login import user_login, user_logout
from .views.signup import user_signup
from main.views.cat import professionals_by_profession, separate_profession
from main.views.community_entry import request_community_entry, verify_community_member, community_entry_success
from main.views.search import search
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', RedirectView.as_view(url='/main/')),
    path('', RedirectView.as_view(url='main/', permanent=True)),
    path("main/", home, name='home'),
    path("main/aboutus/", aboutus, name='aboutus'),
    path("main/login/", user_login, name='login'),
    path("main/signup/", user_signup, name='signup'),
    path('main/professionals/<str:profession>/', professionals_by_profession, name='professionals_by_profession'),
    path('main/verify/<str:profession>/<int:user_id>/', verify_community_member, name='verify_community_member'),
    path('main/separate_profession/<str:profession>/', separate_profession, name='separate_profession'),
    path('main/fullview/<int:id>/', FullView, name='full_view'),
    path('main/logout/', user_logout, name='logout'),
    path('main/search/', search, name='search'),
    path('main/entry-success/', community_entry_success, name='community_entry_success'),
    path('main/request-entry/', request_community_entry, name='request_community_entry'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
