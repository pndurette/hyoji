try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

exec(open('hyoji/version.py').read())

setup(
    name='hyoji',
    version=__version__,
    author='Pierre Nicolas Durette',
    author_email='pndurette@gmail.com',
    url='https://github.com/pndurette/hyoji',
    packages=['hyoji'],
    test_suite='tests',
    #scripts=['bin/gtts-cli', 'bin/gtts-cli.py'],
    license='MIT',
    description='TBA',
    long_description=open('README.md').read(),
    install_requires=[
    ],
    classifiers=[
    #      'Environment :: Console',
    #      'Intended Audience :: Developers',
    #      'License :: OSI Approved :: MIT License',
    #      'Operating System :: MacOS :: MacOS X',
    #      'Operating System :: Unix',
    #      'Operating System :: POSIX',
    #      'Operating System :: POSIX :: Linux',
    #      'Programming Language :: Python :: 2.7',
    #      'Programming Language :: Python :: 3.3',
    #      'Programming Language :: Python :: 3.4',
    #      'Topic :: Software Development :: Libraries',
    #      'Topic :: Multimedia :: Sound/Audio :: Speech'
    ],
)
