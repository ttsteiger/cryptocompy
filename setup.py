from setuptools import setup

setup(name='cryptocompy',
      packages=['cryptocompy'],
      version='0.1.dev1',
      description='Simple wrapper for the public Cryptocompare API.',
      keywords = '',
      author='Titian Steiger',
      author_email='titian.steiger@gmail.com',
      url='https://github.com/ttsteiger/cryptocompare-python',
      download_url='https://github.com/ttsteiger/cryptocompare-python/archive/0.1.dev1.tar.gz',
      license='MIT',
      python_requires='>=3',
      install_requires=['datetime', 'json', 'requests', 'time'],)