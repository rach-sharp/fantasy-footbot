import setuptools

setuptools.setup(
    name='Fantasy Premier League Scout',
    version='1.0',
    description='Picks good teams for the UK FPL Fantasy Football game',
    long_description=open('README.md').read().strip(),
    author='Rachel Sharp',
    author_email='rachelsharp.dev@gmail.com',
    url='https://github.com/rachel-sharp/fantasy-scout',
    packages=setuptools.find_packages(),
    install_requires=[],
    license='MIT License',
    zip_safe=False,
    keywords='football',
    classifiers=['Packages', 'Boilerplate'],
    entry_points={
        "console_scripts": [
            "fpl=fantasy_scout.cli_functions:cli_main"
        ]
    },
    data_files=[
        ("cached_api_data", [])
    ]
)
