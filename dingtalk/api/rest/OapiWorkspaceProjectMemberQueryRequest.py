'''
Created by auto_sdk on 2019.09.16
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceProjectMemberQueryRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.members = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.project.member.query'
