'''
Created by auto_sdk on 2020.01.20
'''
from dingtalk.api.base import RestApi
class OapiPbpInstanceGroupMemberUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.sync_param = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.pbp.instance.group.member.update'
