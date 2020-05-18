'''
Created by auto_sdk on 2019.11.04
'''
from dingtalk.api.base import RestApi
class OapiBlackboardListidsRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.query_request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.blackboard.listids'
