# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User,OpenstackVM,VMware_VsphereVM,Template_Iso,Openstack_Iso,VMware_Template,VM_Dir,VM_Store

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display=('id','name','role','group','privilege')

class Template_IsoAdmin(admin.ModelAdmin):
	list_display=('name','operation','bit')

class OpenstackVMAdmin(admin.ModelAdmin):
        list_display=('name','cpu','memory','disk','operation','bit','volume','ip','vstatus')

class VM_DirAdmin(admin.ModelAdmin):
        list_display=('id','dir_name')

class VM_StoreAdmin(admin.ModelAdmin):
        list_display=('id','store_ip','store_name')

admin.site.register(User,UserAdmin)
admin.site.register(OpenstackVM,OpenstackVMAdmin)
#admin.site.register(Location)
#admin.site.register(VMware_Location)
admin.site.register(VMware_VsphereVM)
admin.site.register(Template_Iso,Template_IsoAdmin)
admin.site.register(Openstack_Iso)
admin.site.register(VMware_Template)
#admin.site.register(VMware_VMware)
admin.site.register(VM_Dir,VM_DirAdmin)
admin.site.register(VM_Store,VM_StoreAdmin)
