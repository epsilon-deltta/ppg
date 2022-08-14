from setuptools import setup, find_packages

# requirements.txt for the install_requires kwarg 
import pathlib
import pkg_resources


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]
# README.md
with open("README.md", "r") as f:
    long_description = f.read()
    
setup(
    name="ppg-pre",   # pypi 에 등록할 라이브러리 이름
    version="0.1.3",    # pypi 에 등록할 version (수정할 때마다 version up을 해줘야 함)
    
    author="epsilon (nickN: kokomong)",
    author_email="kokomong1316@gmail.com",
    url="https://github.com/epsilon-deltta/ppg",
    license='MIT',
    description="Simple PPG preprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    python_requires=">= 3.7",
    packages=find_packages(),
    install_requires=install_requires,
    
    test_suite='tests.test_module',
    
    include_package_data=True
    
    #     
    # extras_require={
    #     'PDF':  ["ReportLab>=1.2", "RXP"],
    #     'reST': ["docutils>=0.3"],
    # },
    # entry_points={
    #     "console_scripts": [
    #         "hey = insutance.main:main"
    #     ]
    # }
)
