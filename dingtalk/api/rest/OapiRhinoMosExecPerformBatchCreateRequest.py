'''
Created by auto_sdk on 2020.04.16
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosExecPerformBatchCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.batch_create_operation_req = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.exec.perform.batch.create'
