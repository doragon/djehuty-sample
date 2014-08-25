import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

install_requires = [
    'djehuty>=0.0.4',
    'uWSGI==2.0.6',
]

setup(name='djehutysample',
      version='0.0',
      description='djehutysample',
      long_description=README,
      classifiers=[
          'Programming Language :: Python',
          'Framework :: Pyramid',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
      ],
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=install_requires,
      test_suite='djehutysample',
      entry_points={
          'paste.app_factory': [
              'main = djehutysample:main',
          ],
	  'djehuty.commands': [
	      'mycommand = djehutysample.commands:MyCommand',
          ],
      },
      )
