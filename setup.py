from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['h2o']

setup(
  name='h2o_mlengine',
  version='0.1',
  author = 'Matias Aravena',
  author_email = 'matias@spikelab.xyz',
  install_requires=REQUIRED_PACKAGES,
  packages=find_packages(),
  include_package_data=True,
  description='Scoring h2o models in GCP ML Engine')