from setuptools import find_packages,setup


with open('requirements.txt','r') as file_object:
    libraries=[]
    while True:
        l=file_object.readline().replace('\n','')
        if l!="" and  l!='-e .':
            libraries.append(l)
        else:
            break
print(libraries)

setup(name='sensor',version='0.0.1',author="Rohan Chitale",author_email="rohan.chitale.6@gmail.com",packages=find_packages(),install_requires=libraries)
