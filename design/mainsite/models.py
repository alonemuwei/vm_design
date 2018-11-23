#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


role_choice=((u'L',u'测试组长'),(u'M',u'测试成员'))
group_choice=((u'1',u'广州一组'),(u'2',u'广州二组'),(u'3',u'成都分组'))
privilege_choice=((u'True',u'已授权'),(u'False','未授权'))
class User(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='用户编号')
	name=models.CharField(max_length=20,verbose_name='用户名称')
	password=models.CharField(max_length=20)
	role=models.CharField(max_length=8,choices=role_choice,verbose_name='用户角色')
	group=models.CharField(max_length=8,choices=group_choice,verbose_name='用户组别')
	privilege=models.CharField(max_length=8,choices=privilege_choice,verbose_name='用户权限')
	
	class Meta:
		ordering=('id',)	

vstatus_choice=((u'1',u'开启'),(u'0',u'关闭'))
class OpenstackVM(models.Model):
	name=models.CharField(max_length=50,primary_key=True,verbose_name='虚拟机名字')
	cpu=models.IntegerField()
	memory=models.IntegerField(verbose_name='内存')
	disk=models.IntegerField(verbose_name='磁盘大小')
	operation=models.CharField(max_length=30,verbose_name='操作系统')
	bit=models.IntegerField(verbose_name='位数')
	volume=models.IntegerField()
	ip=models.CharField(max_length=15)
	vstatus=models.CharField(max_length=4,choices=vstatus_choice,verbose_name='状态')

	class Meta:
		ordering=('-vstatus',)

class VM_Dir(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='目录编号')
	dir_name=models.CharField(max_length=50,verbose_name='目录名称')
	
class VM_Store(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='存储主机编号')
	store_ip=models.CharField(max_length=15,verbose_name='IP地址')
	store_name=models.CharField(max_length=50,verbose_name='存储主机名称')

#class Location(models.Model):
#        name=models.CharField(max_length=50)
#        dir_id=models.IntegerField(verbose_name='目录编号')
#        dirname=models.CharField(max_length=50,verbose_name='目录名称')
#        store_ip=models.CharField(max_length=15,verbose_name='IP地址')
#        store_name=models.CharField(max_length=50,verbose_name='存储主机名称')

#class VMware_Location(models.Model):
#        name=models.ForeignKey(Location,on_delete=models.CASCADE)
#        dir_id=models.IntegerField(primary_key=False)

class VMware_VsphereVM(models.Model):
        name=models.CharField(max_length=50)
	cpu=models.IntegerField()
        memory=models.IntegerField()
        disk=models.IntegerField()
        operation=models.CharField(max_length=30)
        bit=models.IntegerField()
        ip=models.CharField(max_length=15)
        vstatus=models.CharField(max_length=4,choices=vstatus_choice)

        class Meta:
                ordering=('-vstatus',)

class Template_Iso(models.Model):
	name=models.CharField(max_length=50,primary_key=True)
	operation=models.CharField(max_length=30)
	bit=models.IntegerField()
	
class Openstack_Iso(models.Model):
	virtual=models.ForeignKey(OpenstackVM,on_delete=models.CASCADE)
	template=models.ForeignKey(Template_Iso,on_delete=models.CASCADE)

class VMware_Template(models.Model):
        virtual=models.ForeignKey(VMware_VsphereVM,on_delete=models.CASCADE)
        template=models.ForeignKey(Template_Iso,on_delete=models.CASCADE)

#class VMware_VMware(models.Model):
#	virtuala=models.ForeignKey(Location,on_delete=models.CASCADE)
#	virtualb=models.CharField(max_length=50,unique=True)
