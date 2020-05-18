'''
Created by auto_sdk on 2020.03.12
'''
from dingtalk.api.base import RestApi
class OapiCrmObjectdataCustomerCreateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.instance = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.crm.objectdata.customer.create'
