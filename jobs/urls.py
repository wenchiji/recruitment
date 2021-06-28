from django.conf.urls import url

from jobs import views

urlpatterns = [
    url(r"^joblist/", views.jobList, name="jobList"),
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail")
]
