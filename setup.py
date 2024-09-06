from setuptools import find_packages, setup

setup(
    name="Oladipupo Ml Project",
    version= '0.0.1',
    author="Taofeek Opeyemi Olawoye",
    author_email= "habephe21@gmail.com",
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'seaborn', 'scikit-learn', 
                      'matplotlib', 'seaborn', 'pillow'],
)