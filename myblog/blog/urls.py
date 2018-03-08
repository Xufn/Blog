from django.conf.urls import url
import views
urlpatterns=[
    #url(r'test',views.test,name='blog_test'),
    url(r'^(\d+)$',views.detail),
    url(r"^home/",views.home, name="blog_home"),
    url(r'^test/', views.Test, name="blog_test"),
    url(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),

]