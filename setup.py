from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_twilio_sdk_layer',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test source files.
        'b_twilio_sdk_layer_test',
        'b_twilio_sdk_layer_test.*'
    ]),
    description=(
        'AWS CDK based lambda layer including Twilio SDK.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'aws-cdk.core>=1.54.0,<2.0.0',
        'aws-cdk.aws_lambda>=1.54.0,<2.0.0',
        'b-cfn-lambda-layer>=1.1.1,<2.0.0'
    ],
    author='Laimonas Sutkus',
    author_email='laimonas.sutkus@biomapas.com',
    keywords='AWS CDK Lambda Layer Twilio',
    url='https://github.com/biomapas/B.TwilioSdkLayer.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
