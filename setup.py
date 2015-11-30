from codecs import open  # To use a consistent encoding
from glob import glob
from os.path import dirname, abspath, join
from sys import prefix

from distutils import sysconfig
from setuptools import setup
from setuptools.command.install import install

here=dirname(abspath(__file__))
site_packages_path = sysconfig.get_python_lib()
vext_files = list(glob("*.vext"))

def _post_install():
    from vext.install import check_sysdeps
    check_sysdeps(join(here, *vext_files))

class CheckInstall(install):
    def run(self):
        self.do_egg_install()
        self.execute(_post_install, [], msg="Check system dependencies:")

# Get the long description from the relevant file
with open(join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vext.pygtk',
    version='0.2.2',
    description='Use system pygtk from a virtualenv',
    long_description=long_description,

    cmdclass={
        'install': CheckInstall,
    },

    url='https://github.com/stuaxo/vext',
    author='Stuart Axon',
    author_email='stuaxo2@yahoo.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='virtualenv pygtk vext',

    install_requires=["vext"],

    # Install pygtk vext
    data_files=[
        (join(prefix, 'share/vext/specs'), vext_files)
    ],

)
