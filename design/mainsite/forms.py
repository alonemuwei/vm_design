# -*- coding: utf-8 -*-

from django import forms
import models

class PostForm(forms.ModelForm):
	class Meta:
		model=models.OpenstackVM
		fields=['name','cpu','memory','disk','operation','bit','volume','ip','vstatus']
	def __init__(self,*args,**kwargs):
		super(PostForm,self).__init__(*args,**kwargs)
		self.fields['name'].label='虚拟机名字'
                self.fields['name']
                self.fields['name']
                self.fields['name']
                self.fields['name']
                self.fields['name']
                self.fields['name']
                self.fields['name']
                self.fields['name']
