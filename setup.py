from setuptools import setup

setup(
    name='AutoMLOps',
    version='1.0.0',    
    description='AutoMLOps is a tool that generates a production-style \
        MLOps pipeline from Jupyter Notebooks.',
    url='https://source.cloud.google.com/sandbox-srastatter/1-ClickMLOps',
    author='Sean Rastatter',
    author_email='srastatter@google.com',
    license='Apache-2.0',
    packages=['AutoMLOps'],
    install_requires=['autoflake==2.0.0',
                      'pipreqs==0.4.11',
                      'ipython==8.5.0',
                      'PyYAML==5.4.1'],
    classifiers=[
        'Development Status :: Draft',
        'Intended Audience :: data science practitioners',
        'License :: OSI Approved :: Apache-2.0',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',])