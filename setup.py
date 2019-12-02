from setuptools import setup

setup(name='generic-python',
      version='0.0.1',
      description='Python server for Jaqpot pretrained models',
      url='https://github.com/KinkyDesign/generic-python',
      author='Pantelis Karatzas, Pantelis Sopasakis',
      author_email='pantelispanka@gmail.com',
      license='GNU General Public License v3.0',
      packages=['generic-python'],
      install_requires=[
            'tornado', 'pandas'
      ],
      zip_safe=False)