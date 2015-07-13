import setuptools

PACKAGES = ['oca']

setuptools.setup(name='oca',
                 description="OCA maintainer tools",
                 setup_requires=['pbr'],
                 pbr=True,
                 package_data={'': ['*.yaml']})
