'''
Created by auto_sdk on 2019.09.24
'''
from dingtalk.api.base import RestApi
class OapiChatMemberFriendswitchUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.chatid = None
		self.is_prohibit = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.chat.member.friendswitch.update'
