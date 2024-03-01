import requests

class ParchmentSeeker:
    dorks = []
    urls = []

    def __init__(self, urls=None, dorks=None):
        if urls is not None:
            self.urls = urls

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

        extensions = ['.php', '.asp', '.html']

        if len(self.urls) == 0:
            raise ValueError("The list of URLs is empty")

        for link in self.urls:
            for dork in self.dorks:
                for ext in extensions:
                    page = link + dork + ext

                    try:
                        response = requests.get(page, timeout=10)
                        response.raise_for_status()

                    except requests.exceptions.HTTPError:
                        print(f'Unexpected HTTP error at: {page} STATUS: {response.status_code}\n')
                        continue

                    print(f'Admin panel found at: {page} STATUS: {response.status_code}\n')

if __name__ == '__main__':
    domains = ['']
    pf = ParchmentSeeker(domains)
    try:
        pf.request()
    except ValueError:
        ...
