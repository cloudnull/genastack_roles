# =============================================================================
# Copyright [2013] [Kevin Carter]
# License Information :
# This software has no warranty, it is provided 'as is'. It is your
# responsibility to validate the behavior of the routines and its accuracy
# using the code provided. Consult the GNU General Public license for further
# details (see GNU General Public License).
# http://www.gnu.org/licenses/gpl.html
# =============================================================================
from genastack.common import utils


ARGS = utils.get_role_config('ceilometer')
BRANCH = ARGS.get('branch', 'master')
PROJECT_URL = ARGS.get(
    'project_url', 'https://github.com/openstack/ceilometer.git'
)


BUILD_DATA = {
    'ceilometer': {
        'use_system_python': ARGS.get('use_system_python', False),
        'help': 'Install Ceilometer from upstream on Branch "%s"' % BRANCH,
        'required': [
            'python',
            'ceilometer_client',
            'keystone_client',
            'ceilometer_client',
            'trove_client'
        ],
        'directories': [
            {
                'path': '/var/log/ceilometer',
                'user': 'ceilometer',
                'group': 'ceilometer',
                'mode': '0755'
            },
            {
                'path': '/var/lib/ceilometer',
                'user': 'ceilometer',
                'group': 'ceilometer',
                'mode': '0755'
            },
            {
                'path': '/etc/ceilometer',
                'user': 'ceilometer',
                'group': 'ceilometer',
                'mode': '0755'
            }
        ],
        'group_create': [
            {
                'group': 'ceilometer',
                'system': True
            }
        ],
        'user_create': [
            {
                'user': 'ceilometer',
                'group': 'ceilometer',
                'home': '/var/lib/ceilometer',
                'system': True
            }
        ],
        'git_install': [
            {
                'name': 'ceilometer',
                'project_url': PROJECT_URL,
                'branch': BRANCH,
                'config_example': 'etc/ceilometer=/etc/ceilometer',
                'group_owner': 'ceilometer',
                'user_owner': 'ceilometer',
                'mode': '0644'
            }
        ],
        'package_install': {
            'apt': {
                'packages': [
                    'mysql-client',
                    'libmysqlclient-dev'
                ]
            }
        }
    }
}
