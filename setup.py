#!/usr/bin/env python
install_requires = ['numpy','pandas','python-dateutil','pytz',
    'sciencedates']
tests_require=['nose','coveralls']
# %%
from setuptools import setup,find_packages

setup(name='AEindex_plot',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/AE-index-plot',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: GNU Affero License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python :: 3',
      ],
      install_requires=install_requires,
      extras_require={'plot':['matplotlib','seaborn',],
                      'tests':tests_require},
      python_requires='>=3.5',
      tests_require=tests_require,
	  )
