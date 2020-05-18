'''
Created by auto_sdk on 2020.04.23
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosLayoutOperationdefsListsimpleRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.operation_uids = None
		self.tenant_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.layout.operationdefs.listsimple'
