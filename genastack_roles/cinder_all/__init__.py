# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================


BUILD_DATA = {
    'cinder_all': {
        'help': 'Install all of Cinder from upstream',
        'required': [
            'cinder_client',
            'cinder_api',
            'cinder_scheduler',
            'cinder_volume'
        ]
    }
}
