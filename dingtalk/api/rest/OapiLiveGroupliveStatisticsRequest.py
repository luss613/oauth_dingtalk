'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiLiveGroupliveStatisticsRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.cid = None
		self.live_uuid = None
		self.open_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.live.grouplive.statistics'
