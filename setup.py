#!/usr/bin/env python

req = ['nose','numpy','pandas','matplotlib','seaborn','python-dateutil','pytz']
pipreq=['sciencedates']
# %%
import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except Exception as e:
    pip.main(['install'] + req)
pip.main(['install'] + pipreq)
# %%
from setuptools import setup

setup(name='AEindex_plot',
      packages=['aeindex'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/AE-index-plot',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: GNU Affero License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python :: 3',
      ],
      install_requires=req+pipreq,
	  )
