from setuptools import setup, find_packages

setup(
    name='morbid',
    version='0.8.7.3',
    author='Michael Carter',
    author_email='CarterMichael@gmail.com',
    license='MIT License',
    install_requires = ['stomper'],
    description='A Twisted-based publish/subscribe messaging server that uses the STOMP protocol',
    packages= find_packages(),
    entry_points = '''
        [console_scripts]
        morbid = morbid:main
        morbid_restq_test = morbid.sample_restq.restq_dummy_daemon:main
    ''',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
