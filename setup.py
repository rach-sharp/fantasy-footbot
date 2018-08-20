import setuptools

setuptools.setup(
    name='footbot',
    version='0.1.1',
    description='Picks good teams for the UK FPL Fantasy Football game',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    author='Rachel Sharp',
    author_email='rachelsharp.dev@gmail.com',
    url='https://github.com/rach-sharp/fantasy-footbot',
    packages=setuptools.find_packages(),
    install_requires=['clint', 'requests', 'pulp'],
    license='MIT License',
    zip_safe=False,
    keywords='football',
    classifiers=[],
    entry_points={
        "console_scripts": [
            "footbot=fantasy_footbot.cli_functions:cli_main"
        ]
    },
    data_files=[
        ("cached_api_data", [])
    ],
)
