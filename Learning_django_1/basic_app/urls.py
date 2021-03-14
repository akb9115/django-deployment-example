from django.urls import path,re_path
from basic_app import views
from django.conf.urls import include

# TEMPLATE TAGGING

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$',views.relative,name="relative"),
    re_path(r'^other/$',views.other,name="other"),
    re_path(r'^studentregs/$',views.studentRegs,name="studentregs"),
    path('deleteStudent/<int:roll>/',views.deleteStudent,name="deleteStudent")
]