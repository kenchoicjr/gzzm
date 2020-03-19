from django.contrib import admin
from django.conf.urls import url, include
import customerservice.views

app_name = 'customerservice'

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', customerservice.views.weixin_main),
    url(r'index/', customerservice.views.index),
    url(r'login/', customerservice.views.login),
    url(r'schools_list/', customerservice.views.schools_list),
    url(r'order_list/', customerservice.views.order_list),
    url(r'logout/', customerservice.views.logout),
    url(r'getCity/', customerservice.views.getCity),
    url(r'schools_list_add/', customerservice.views.schoolAdd),
    url(r'schools_list_edit/', customerservice.views.schoolEdit),
    url(r'schools_list_edit_save/', customerservice.views.schoolEditSave),
    url(r'terminial_list_add/', customerservice.views.terminialAdd),
    url(r'terminial_list_edit/', customerservice.views.terminialEdit),
    url(r'terminial_list_edit_save/', customerservice.views.terminialEditSave),
    url(r'terminial_list/(\d+)$', customerservice.views.terminial_list),
    url(r'order_edit/', customerservice.views.order_edit),
    url(r'order_add/', customerservice.views.order_add),
    url(r'order_add_save/', customerservice.views.order_add_save),
    url(r'termail_a/', customerservice.views.termail_a),
    url(r'classification_a/', customerservice.views.classification_a),
    url(r'order_edit_save/', customerservice.views.order_edit_save),
]
