'''
Created by auto_sdk on 2020.05.07
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceTaskCleanRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentid = None
		self.corp_id = None
		self.operator_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.task.clean'
