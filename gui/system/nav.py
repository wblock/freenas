from django.utils.translation import ugettext_lazy as _
from freenasUI.freeadmin.tree import TreeNode
from freenasUI.middleware.notifier import notifier

BLACKLIST = [
    'NTPServer',
    'CertificateAuthority',
    'Certificate'
]
NAME = _('System')
ICON = u'SystemIcon'
ORDER = 1


class Advanced(TreeNode):

    gname = 'Advanced'
    name = _(u'Advanced')
    icon = u"SettingsIcon"
    type = 'opensystem'
    order = -90
    replace_only = True
    append_to = 'system'


class BootEnv(TreeNode):

    gname = 'BootEnv'
    name = _(u'Boot')
    icon = 'BootIcon'
    type = 'opensystem'
    order = -92


class CloudCredentials(TreeNode):

    gname = 'CloudCredentials'
    replace_only = True
    append_to = 'system'

    def pre_build_options(self):
        if not notifier().is_freenas():
            return
        raise ValueError


class Email(TreeNode):

    gname = 'Email'
    name = _(u'Email')
    icon = 'EmailIcon'
    type = 'opensystem'
    order = -85
    replace_only = True
    append_to = 'system'


class General(TreeNode):

    gname = 'Settings'
    name = _(u'General')
    icon = u"SettingsIcon"
    type = 'opensystem'
    order = -95
    replace_only = True
    append_to = 'system'


class Info(TreeNode):

    gname = 'SysInfo'
    name = _(u'Information')
    icon = u"InfoIcon"
    type = 'opensystem'
    order = -100


class SystemDataset(TreeNode):

    gname = 'SystemDataset'
    name = _(u'System Dataset')
    icon = u"SysDatasetIcon"
    type = 'opensystem'
    order = -80
    replace_only = True
    append_to = 'system'


class TunableView(TreeNode):

    gname = 'View'
    type = 'opensystem'
    append_to = 'system.Tunable'


class Update(TreeNode):

    gname = 'Update'
    name = _('Update')
    type = 'opensystem'
    icon = 'UpdateIcon'


class CertificateAuthorityView(TreeNode):

    gname = 'CertificateAuthority.View'
    name = _('CAs')
    type = 'opensystem'
    icon = u'CertificateAuthorityIcon'
    order = 10


class CertificateView(TreeNode):

    gname = 'Certificate.View'
    name = _('Certificates')
    type = 'opensystem'
    icon = u'CertificateIcon'
    order = 15


class Support(TreeNode):

    gname = 'Support'
    name = _(u'Support')
    icon = u"SupportIcon"
    type = 'opensystem'
    order = 20
