'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class OapiImpaasUserGetprofileRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.impaas.user.getprofile'
