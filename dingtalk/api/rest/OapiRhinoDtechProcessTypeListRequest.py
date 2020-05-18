'''
Created by auto_sdk on 2020.03.09
'''
from dingtalk.api.base import RestApi
class OapiRhinoDtechProcessTypeListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.dtech.process.type.list'
