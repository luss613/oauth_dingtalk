'''
Created by auto_sdk on 2020.04.24
'''
from dingtalk.api.base import RestApi
class OapiSmartworkHrmEmployeeFieldGrouplistRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartwork.hrm.employee.field.grouplist'
