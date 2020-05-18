'''
Created by auto_sdk on 2020.03.11
'''
from dingtalk.api.base import RestApi
class OapiRhinoDtechMachineParamListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.biz_id_process_list = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.dtech.machine.param.list'
