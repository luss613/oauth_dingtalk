'''
Created by auto_sdk on 2019.11.19
'''
from dingtalk.api.base import RestApi
class OapiCalendarV2EventCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentid = None
		self.event = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.calendar.v2.event.create'
