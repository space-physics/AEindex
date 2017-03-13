#!/usr/bin/env python
from setuptools import setup

req = ['nose','numpy','pandas','matplotlib','seaborn','python-dateutil','pytz',
       'sciencedates']

#%% install
setup(name='AEindex_plot',
      packages=['aeindex'],
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/AE-index-plot',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: GNU Affero License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python :: 3.6',
      ],
      install_requires=req,
	  )
