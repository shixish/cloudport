from django.conf.urls.defaults import *
#from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    #(r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^req/', 'cloudport.job_manager.views.req_data'),
    (r'^success/(.*)', 'cloudport.job_manager.views.success'),
    (r'^upload', 'cloudport.job_manager.views.upload_file'),
    (r'^', 'cloudport.job_manager.views.manager'),
)
