from __future__ import absolute_import
from django.utils.translation import ugettext as _
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse

from .base import BaseAdminView, filter_hook
from .dashboard import Dashboard
from xadmin.forms import AdminAuthenticationForm
from xadmin.models import UserSettings
from xadmin.layout import FormHelper


class IndexView(Dashboard):
    title = _("Main Dashboard")
    icon = "fa fa-dashboard"

    def get_page_id(self):
        return 'home'


class UserSettingView(BaseAdminView):

    @never_cache
    def post(self, request):
        key = request.POST['key']
        val = request.POST['value']
        us, created = UserSettings.objects.get_or_create(
            user=self.user, key=key)
        us.value = val
        us.save()
        return HttpResponse('')


class LoginViewView(BaseAdminView):

    title = _("Please LoginView")
    LoginView_form = None
    LoginView_template = None

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        helper = FormHelper()
        helper.form_tag = False
        helper.include_media = False
        context.update({
            'title': self.title,
            'helper': helper,
            'app_path': request.get_full_path(),
            REDIRECT_FIELD_NAME: request.get_full_path(),
        })
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'authentication_form': self.LoginView_form or AdminAuthenticationForm,
            'template_name': self.LoginView_template or 'xadmin/views/LoginView.html',
        }
        self.update_params(defaults)
        return LoginView(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)


class LogoutViewView(BaseAdminView):

    LogoutView_template = None
    need_site_permission = False

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'template_name': self.LogoutView_template or 'xadmin/views/logged_out.html',
        }
        if self.LogoutView_template is not None:
            defaults['template_name'] = self.LogoutView_template

        self.update_params(defaults)
        return LogoutView(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)
