"""oldschoolmtgdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from decks import views

urlpatterns = [
    url(r'^$', views.TournamentsListView.as_view(), name='home'),
    url(r'^signup/$',
        accounts_views.signup,
        name='signup'),
    url(r'^login/$',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(),
        name='logout'),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/account/$',
        accounts_views.UserUpdateView.as_view(),
        name='my_account'),
    url(r'^settings/password/$',
        auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^tournaments/(?P<pk>[0-9A-Za-z_\-]+)/$',
        views.DeckListView.as_view(),
        name='deck_tournaments'),
    url(r'^tournaments/(?P<pk>\d+)/decks/(?P<deck_pk>\d+)/$',
        views.CardListView.as_view(),
        name='deck_cards'),
    url(r'^admin/', admin.site.urls),
]
