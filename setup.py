from setuptools import setup,find_packages

def main():
        setup(name='pzaif',
              version='1.0',
              author="safari029",
              py_module='pzaif',
              packages=find_packages("src"),
              url=["https://github.com/safari029/pzaif"],
              install_requires=['requests'],
              )

if __name__=='__main__':
        main()