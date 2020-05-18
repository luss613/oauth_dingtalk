'''
Created by auto_sdk on 2019.11.30
'''
from dingtalk.api.base import RestApi
class OapiSmartappFormInstanceAddRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.app_uuid = None
		self.data_list = None
		self.form_code = None
		self.operator_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartapp.form.instance.add'
