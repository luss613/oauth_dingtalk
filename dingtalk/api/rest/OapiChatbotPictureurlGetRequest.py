'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiChatbotPictureurlGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.download_code = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.chatbot.pictureurl.get'
