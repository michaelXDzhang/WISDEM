#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

setup(
    name='WISDEM',
    version='0.1.0',
    description='Wind-Plant Integrated System Design & Engineering Model',
    author='K. Dykes and S. Andrew Ning',
    author_email='katherine.dykes@nrel.gov',
    install_requires=['fusedwind','commonse', 'drivese','drivewpact','plant_costsse','plant_energyse','plant_financese','rotorse','towerse', 'turbine_costsse'],
    package_data= {'WISDEM': []},
    package_dir= {'': 'src'},
    packages= ['wisdem.lcoe','test','wisdem.turbinese'],
    license='Apache License, Version 2.0',
    dependency_links=[#'https://github.com/WISDEM/CommonSE/tarball/master#egg=fusedwind', #need to update fusedwind repository name
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=commonse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=drivese',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=drivewpact',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=plant_costsse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=plant_energyse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=plant_financese',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=rotorse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=towerse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=turbine_costsse',
        'https://github.com/WISDEM/CommonSE/tarball/master#egg=turbinese',
        ],
    zip_safe=False
)
