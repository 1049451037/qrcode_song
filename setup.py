from setuptools import setup

setup(name='qrcode_song',
      version='0.3',
      description='A qrcode generator based on cli-qrcode and web crawler.',
      url='https://github.com/1049451037/qrcode_song',
      download_url = 'https://github.com/1049451037/qrcode_song/archive/0.3.tar.gz',
      author='Qingsong Lv',
      author_email='lqs@mail.bnu.edu.cn',
      license='MIT',
      packages=['qrcode_song'],
      install_requires=[
          'requests',
          'beautifulsoup4',
      ],
      zip_safe=False)