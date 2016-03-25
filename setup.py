from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(name='py',
      version=version,
      description="shell dict tool",
      long_description="""shell dict tool""",
      classifiers=[],
      keywords='python iciba dictionary terminal',
      author='huangpeng',
      author_email='huangpeng_coding@163.com',
      url='https://github.com/huangpengCoding',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'termcolor',
      ],
      entry_points={
          'console_scripts': [
              'fy = fy.fy:main'
          ]
      },
      )
