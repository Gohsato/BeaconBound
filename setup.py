import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='beaconbound',  
     version='0.1.0',
     author="Goh Sato",
     author_email="goh.sato@outlook.com",
     description="A finder of beacons2",
     packages=["src"],
     install_requires=[
        "cycler==0.10.0",
        "kiwisolver==1.0.1",
        "matplotlib==3.0.2",
        "numpy==1.16.0",
        "opencv-contrib-python==4.0.0.21",
        "pyparsing==2.3.1",
        "python-dateutil==2.7.5",
        "six==1.12.0",
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )