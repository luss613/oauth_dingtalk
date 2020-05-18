'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiBipaasMenuAddReportRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.antcloud_tenant_id = None
		self.menu_id = None
		self.report_ids = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.bipaas.menu.add_report'
