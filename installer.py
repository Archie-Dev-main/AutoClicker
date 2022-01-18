import pip
import pkg_resources

# Checks if the modules this program needs are installed and then installs them with pip if they aren't
class Installer:
    def install_required_modules(self):
        # Contains a list with the module names to be check and/or installed
        for package in ['mouse', 'Pillow']:
            try:
                dist = pkg_resources.get_distribution(package)
                print('{} ({}) is installed'.format(dist.key, dist.version))
            except pkg_resources.DistributionNotFound:
                print('{} is NOT installed'.format(package))
                pip.main(['install', package])