'''
Created by auto_sdk on 2019.12.03
'''
from dingtalk.api.base import RestApi
class OapiChatbotInstallRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.chatbot_vo = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.chatbot.install'
