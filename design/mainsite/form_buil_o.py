# -*- coding: utf-8 -*-

from django import forms
from mainsite import models

class PostForm(forms.ModelForm):
	class Meta:
		model=models.OpenstackVM
		fields=['name','cpu','memory','disk','operation','bit','volume','ip','vstatus']
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['name'].label='虚拟机名字'
                self.fields['cpu'].label='CPU数量'
                self.fields['memory'].label='内存'
                self.fields['disk'].label='磁盘大小'
                self.fields['operation'].label='操作系统'
                self.fields['bit'].label='位数'
                self.fields['volume'].label='卷大小'
                self.fields['ip'].label='IP地址'
                self.fields['vstatus']='是否开启虚拟机'
