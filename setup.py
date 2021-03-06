from setuptools import setup, find_packages

setup(
    name='gnma',
    version='0.1',
    platforms=("Windows", "Linux", "Mac OS-X", "Unix",),
    keywords="molecular dynamics structure analysis",
    author="Carlos Xavier Hernández",
    author_email="cxh@stanford.edu",
    url='https://github.com/cxhernandez/gnma',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['README.md',
             'requirements.txt'],
    },
    zip_safe=False,
)
