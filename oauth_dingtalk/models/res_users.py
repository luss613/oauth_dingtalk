# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 PaulLu LGPL-3
###################################################################################

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning, AccessDenied


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def auth_oauth_dingtalk(self, code, user):
        user_ids = self.env['hr.employee'].search([('mobile_phone', '=', user.get('mobile'))]).mapped('user_id')
        res_users = self.search([('id', 'in', user_ids.ids)])
        if not res_users or len(res_users) > 1:
            return AccessDenied
        return (self.env.cr.dbname, res_users.login, user.get('mobile'))

    @api.model
    def _check_credentials(self, password):
        try:
            return super(ResUsers, self)._check_credentials(password)
        except AccessDenied:
            res = self.env['hr.employee'].sudo().search(
                [('user_id', '=', self.env.uid), ('mobile_phone', '=', password)])
            if not res:
                raise
