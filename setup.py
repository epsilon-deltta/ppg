from setuptools import setup, find_packages

# Reference requirements.txt for the install_requires kwarg 
import pathlib
import pkg_resources


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="ppg-pre",   # pypi 에 등록할 라이브러리 이름
    version="0.1",    # pypi 에 등록할 version (수정할 때마다 version up을 해줘야 함)
    
    description="Simple PPG preprocessing",
    author="epsilon (nickN: kokomong)",
    author_email="kokomong1316@gmail.com",
    url="https://github.com/epsilon-deltta/ppg",
    license='MIT',
    
    python_requires=">= 3.7",
    packages=find_packages(),
    install_requires=install_requires,

    # 중요한 부분
    # entry_points={
    #     "console_scripts": [
    #         "hey = insutance.main:main"
    #     ]
    # }
)