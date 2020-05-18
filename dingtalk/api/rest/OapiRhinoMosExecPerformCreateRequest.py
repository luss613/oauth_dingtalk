'''
Created by auto_sdk on 2020.03.23
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosExecPerformCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.operations = None
		self.tenant_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.exec.perform.create'
