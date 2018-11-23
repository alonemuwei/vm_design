# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime
from .models import User,OpenstackVM,Template_Iso,Openstack_Iso,VMware_Template,VM_Dir,VM_Store
from mainsite import forms
# Create your views here.

def login(request):
	template=get_template('login.html')
	try:
		urid=request.GET['user_id']
		urpass=reuqest.GET['user_passwd']
	except:
		urid = None
	if urid != None and urpass != None:
		verified=True
	else:
		verified=False
        html=template.render(locals())
        return HttpResponse(html)
def showuser(request):
	users=User.objects.all()
	template=get_template('user.html')
	html=template.render(locals())
	return HttpResponse(html)
def showuser_o(request):
        users=User.objects.all()
        template=get_template('user_o.html')
        html=template.render(locals())
        return HttpResponse(html)

def showbuild(request):
        template=get_template('build.html')
	iso=Template_Iso.objects.all()
	vm_dir=VM_Dir.objects.all()
	vm_store=VM_Store.objects.all()
	cpu=range(1,17)
	bit=[32,64]
	memory=range(1,9)
#	try:
#                o_name=request.GET['name']
#		o_directory=request.GET['directory']
#		o_store_ip=request.GET['store_ip']
#		o_store_name=request.GET['store_name']
#                o_iso=request.GET['iso']
#                o_cpu=request.GET['cpu']
#                o_memory=request.GET['memory']
#                o_disk=request.GET['disk']
#                o_bit=request.GET['bit']
#                o_ip=request.GET['ip']
#		a=VM_Dir.objects.get(dir_name='o_directory')
#		o_dir_id=a.id
#        except:
#                o_name=None
#                o_ip=None
#		o_disk=None
#        if o_name !=None and (o_ip != None and o_disk != None):
#		a=VM_Dir.objects.get(dir_name='o_directory')
#		o_dir_id=a.id
#		l=Location.objects.create(name=o_name,dir_id=o_dir_id,dir_name=o_directory,store_ip=o_store_ip,store_name=o_store_name)
#		l.save()
#                p=VMware_VsphereVM.objects.create(name=o_name,cpu=o_cpu,memory=o_memory,disk=o_disk,operation=o_iso,bit=o_bit,ip=o_ip,vstatus='1')
#                p.save()

        html=template.render(locals())
        return HttpResponse(html)

def showbuild_o(request):
        template=get_template('build_o.html')
	iso=Template_Iso.objects.all()
	disk=[60,200]
	cpu=[1,2,4]
	memory=[1,2,4]
	bit=[32,64]
	try:
		o_name=request.GET['name']
		o_iso=request.GET['iso']
		o_cpu=request.GET['cpu']
		o_memory=request.GET['memory']
		o_disk=request.GET['disk']
		o_bit=request.GET['bit']
		o_ip=request.GET['ip']
		o_volume=request.GET['volume']
	except:
		o_name=None
		o_ip=None
	if o_name !=None and o_ip != None:
		p=OpenstackVM.objects.create(name=o_name,cpu=o_cpu,memory=o_memory,disk=o_disk,operation=o_iso,bit=o_bit,volume=o_volume,ip=o_ip,vstatus='1')
		p.save() 
	html=template.render(locals())
	return HttpResponse(html)

def showclone(request):
        template=get_template('clone.html')
	html=template.render(locals())
	return HttpResponse(html)
def showvm(request):
        template=get_template('vm.html')
        html=template.render(locals())
        return HttpResponse(html)

def showvm_o(request):
        template=get_template('vm_o.html')
	openstack_vm=OpenstackVM.objects.all().order_by('ip')
        html=template.render(locals())
        return HttpResponse(html)

def delvm(request):
	template=get_template('del.html')
	try:
           vm_name=request.GET['vmname']
        except:
           vm_name=None
        if vm_name !=None:
           a=OpenstackVM.objects.filter(name=vm_name).delete()
        html=template.render(locals())
        return HttpResponse(html)

def closevm(request):
        template=get_template('close.html')
	try:
	   vm_name=request.GET['vmname']
	except:
	   vm_name=None
	if vm_name !=None:
 	   a=OpenstackVM.objects.filter(name=vm_name).update(vstatus='0')
        html=template.render(locals())
        return HttpResponse(html)

def openvm(request):
    template=get_template('open.html')
    try:
        vm_name=request.GET['vmname']
    except:
	vm_name=None
    if vm_name !=None:
	a=OpenstackVM.objects.filter(name=vm_name).update(vstatus='1')
#	a.save()
    html=template.render(locals())
    return HttpResponse(html)



def index(request):
	template=get_template('index.html')
        users=User.objects.all()
        now=datetime.now()
        html=template.render(locals())
        return HttpResponse(html)
def index_o(request):
        template=get_template('index_o.html')
        users=User.objects.all()
        now=datetime.now()
        html=template.render(locals())
        return HttpResponse(html)

def vmpart(request):
        template=get_template('vmpart.html')
        html=template.render(locals())
        return HttpResponse(html)

