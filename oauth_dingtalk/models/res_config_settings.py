# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 PaulLu LGPL-3
###################################################################################

import logging
from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    dingtalk_qrKey = fields.Char(u'钉钉扫码appKey')
    dingtalk_qrSecret = fields.Char(u'钉钉扫码appSecret')
    dingtalk_appKey = fields.Char(u'钉钉应用appkey')
    dingtalk_appSecret = fields.Char(u'钉钉应用appSecret')

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            dingtalk_qrKey=self.env['ir.config_parameter'].sudo().get_param(
                'oauth_dingtalk.qrKey') or '',
            dingtalk_qrSecret=self.env['ir.config_parameter'].sudo().get_param(
                'oauth_dingtalk.qrSecret') or '',
            dingtalk_appKey=self.env['ir.config_parameter'].sudo().get_param(
                'oauth_dingtalk.appKey') or '',
            dingtalk_appSecret=self.env['ir.config_parameter'].sudo().get_param(
                'oauth_dingtalk.appSecret') or ''
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('oauth_dingtalk.qrKey', self.dingtalk_qrKey)
        self.env['ir.config_parameter'].sudo().set_param('oauth_dingtalk.qrSecret', self.dingtalk_qrSecret)
        self.env['ir.config_parameter'].sudo().set_param('oauth_dingtalk.appKey', self.dingtalk_appKey)
        self.env['ir.config_parameter'].sudo().set_param('oauth_dingtalk.appSecret', self.dingtalk_appSecret)
