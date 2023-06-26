from django.urls import path

from .views import index, post, about, post_all, cv, postPersonal, postPersonal_all, search, searchPersonal, postcategories

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug>/', post, name = 'post'),
    path('post-all/', post_all, name = 'post-all'),
    path('about/', about, name = 'about' ),
    path('cv/', cv, name = 'cv' ),
    path('until-our-next-meeting/<slug>/', postPersonal, name = 'postPersonal'),
    path('until-our-next-meeting-all/', postPersonal_all, name = 'postPersonal-all'),
    path('search/', search, name = 'search'),
    path('searchPP/', searchPersonal, name = 'searchPersonal'),
    path('post-categories/<slug>/', postcategories, name = 'post-categories'), 
]