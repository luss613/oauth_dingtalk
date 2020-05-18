# -*- coding: utf-8 -*-
###################################################################################
#    Copyright (C) 2020 PaulLu LGPL-3
###################################################################################
import logging
import werkzeug
import dingtalk.api
from werkzeug.exceptions import BadRequest
from odoo import api, http, _
from odoo.addons.auth_oauth.controllers.main import OAuthController as Controller
from odoo.exceptions import AccessDenied
from odoo.http import request

_logger = logging.getLogger(__name__)


class OAuthController(Controller):

    @http.route('/web/dingtalk/login', type='http', auth='public', website=True)
    def web_dingtalk_qr_login(self, **kw):
        params = request.env['ir.config_parameter'].sudo()
        qrKey = params.get_param('oauth_dingtalk.qrKey', default='')
        web_base_url = params.get_param('web.base.url', default='')
        url = '{}/web/dingtalk/qr/action'.format(web_base_url)
        data = {'url': url, 'qrKey': qrKey}
        return request.render('oauth_dingtalk.qr_login_signup', data)

    @http.route('/web/dingtalk/redirect', type='http', auth='public', website=True)
    def redirect_to_dingtalk(self, **kw):
        params = request.env['ir.config_parameter'].sudo()
        qrKey = params.get_param('oauth_dingtalk.qrKey', default='')
        web_base_url = params.get_param('web.base.url', default='')
        redirect_url = '{}/web/dingtalk/qr/action'.format(web_base_url)
        url = "https://oapi.dingtalk.com/connect/oauth2/sns_authorize?appid={}&response_type=code&scope=snsapi_login&state=STATE&redirect_uri={}&loginTmpCode={}".format(
            qrKey, redirect_url, kw.get('loginTmpCode'))
        return http.redirect_with_hash(url)

    @http.route('/web/dingtalk/qr/action', type='http', auth='none')
    def web_dingtalk_qr_login_action(self, **kw):
        code = kw.get('code')
        token = self.get_token()
        userinfo = self.get_userinfo_bycode(code)
        userid = self.get_userid_by_unionid(token, userinfo['unionid'])
        user = self.get_user(token, userid)
        employee = request.env['hr.employee'].sudo().search([('mobile_phone', '=', user.get('mobile'))], limit=1)
        if not employee:
            return http.redirect_with_hash("/web/login?oauth_error=2")
        try:
            credentials = request.env['res.users'].sudo().auth_oauth_dingtalk(code, user)
            url = '/web'
            uid = request.session.authenticate(*credentials)
            if uid is not False:
                request.params['login_success'] = True
                return http.redirect_with_hash(url)
        except AttributeError as ae:
            url = "/web/login?oauth_error=1"
        except AccessDenied:
            url = "/web/login?oauth_error=3"
            redirect = werkzeug.utils.redirect(url, 303)
            redirect.autocorrect_location_header = False
            return redirect
        except Exception as e:
            _logger.exception("OAuth2: %s" % str(e))
            url = "/web/login?oauth_error=2"
        return http.redirect_with_hash(url)

    def get_token(self):
        params = request.env['ir.config_parameter'].sudo()

        appkey = params.get_param('oauth_dingtalk.appKey', default='')
        appscret = params.get_param('oauth_dingtalk.appSecret', default='')
        if not appkey or not appscret:
            raise werkzeug.exceptions.Forbidden(u'Should setting appKey Or appSecret first.')

        url = "https://oapi.dingtalk.com/gettoken"

        t = dingtalk.api.OapiGettokenRequest(url)
        t.appkey = appkey
        t.appsecret = appscret
        try:
            token = t.getResponse()
            return token['access_token']
        except Exception as e:
            raise werkzeug.exceptions.Forbidden(e.errmsg)

    def get_userinfo_bycode(self, code):
        params = request.env['ir.config_parameter'].sudo()

        qrKey = params.get_param('oauth_dingtalk.qrKey', default='')
        qrSecret = params.get_param('oauth_dingtalk.qrSecret', default='')
        url = 'https://oapi.dingtalk.com/sns/getuserinfo_bycode'
        if not qrKey or not qrSecret:
            raise werkzeug.exceptions.NotFound()
        result = dingtalk.api.OapiSnsGetuserinfoBycodeRequest(url)
        result.tmp_auth_code = code
        try:
            user = result.getResponse(accessKey=qrKey, accessSecret=qrSecret)
            return user['user_info']
        except Exception as e:
            raise werkzeug.exceptions.Forbidden(e.errmsg)

    def get_userid_by_unionid(self, token, unionid):
        params = dict(access_token=token, unionid=unionid)
        url = 'https://oapi.dingtalk.com/user/getUseridByUnionid'
        user = dingtalk.api.OapiUserGetUseridByUnionidRequest(url)
        user.unionid = unionid
        try:
            result = user.getResponse(authrize=token)
            return result['userid']
        except Exception as e:
            raise werkzeug.exceptions.Forbidden(e.errmsg)

    def get_user(self, token, userid):
        url = "https://oapi.dingtalk.com/user/get"

        user = dingtalk.api.OapiGettokenRequest(url)
        user.userid = userid
        try:
            result = user.getResponse(authrize=token)
            return result
        except Exception as e:
            raise werkzeug.exceptions.Forbidden(e.errmsg)
