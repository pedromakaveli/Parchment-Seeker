'''

Module for searching admin panels on given URLs using ParchmentSeeker class.

'''

import requests


class ParchmentSeeker:
    '''
    A class to seek admin panels on given URLs.

    Attributes:
        dorks (list): A list of common admin panel paths to be appended to URLs.
        urls (list): A list of URLs to search for admin panels.

    Methods:
        __init__: Initializes the ParchmentSeeker object.
        request: Tries to find admin panels on the provided URLs.
    '''

    dorks = []
    urls = []
    extensions = []
    founded = []

    def __init__(self, urls=None, dorks=None, extensions=None):

        self.urls = urls

        if extensions is not None:
            self.extensions = extensions
        else:
            self.extensions = ['.php', '.asp', '.html']

        if dorks is not None:
            self.dorks = dorks
        else:
            self.dorks = [
                    'admin', 'administrator', 'administrador',
                    'Admin', 'Administrator', 'Administrador',
                    'wp-admin', 'adminpanel', 'admin_area',
                    'administration', 'admin-login', 'backend',
                    'admincp', 'admin/index', 'admin/login',
                    'administrator/login', 'administrador/login','administrator/index',
                    'administrador/index','controlpanel', 'cpanel',
                    'panel', 'admin_page', 'admin_area/login',
                    'admin_area/admin', 'siteadmin', 'site_admin',
                    'admin/controlpanel', 'admin/adminLogin', 'admin/admin_login',
                    'admin/admin-login', 'admin/adminpanel', 'admin/admin_panel',
                    'admin/home', 'admin_area/admin', 'admin_area/login',
                    'panel-administracion', 'admin/cp', 'cp',
                    'adminpanel/index', 'adminpanel/login', 'adminpanel/admin',
                    'adminpanel/admin-login', 'adminarea'
                ]

    def request(self):
        '''
            Try to find the admin panel
        '''

        if len(self.urls) == 0:
            raise ValueError("The list of URLs is empty")

        if len(self.extensions) == 0:
            raise ValueError("The list of extensions is empty")

        if len(self.dorks) == 0:
            raise ValueError("The list of dorks is empty")

        for link in self.urls:
            for dork in self.dorks:
                for ext in self.extensions:
                    page = link + dork + ext

                    try:
                        response = requests.get(page, timeout=10)
                        response.raise_for_status()

                    except requests.exceptions.HTTPError:
                        print(f'Unexpected HTTP error at: {page} STATUS: {response.status_code}\n')
                        continue

                    except requests.exceptions.Timeout:
                        print(f'The request has timed out at {page}')
                        continue

                    print(f'Admin panel found at: {page} STATUS: {response.status_code}\n')
                    self.founded.append(page)
