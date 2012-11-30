from distutils.core import setup
import setuplib

packages, package_data = setuplib.find_packages(['chunks', 'chunks.templatetags'])

setup(name='chunks',
      version='2.4',
      description='Keyed blocks of content for use in your Django templates',
      author='Clint Ecker',
      author_email='me@clintecker.com',
      url='https://github.com/code-on/django-chunks',
      install_requires=['easy_thumbnails'],
      packages=packages,
      package_data=package_data,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
