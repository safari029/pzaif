from setuptools import setup,find_packages

def main():
        setup(name='pzaif',
              version='2.0.1',
              author="safari029",
              packages=["pzaif"],
              url=["https://github.com/safari029/pzaif"],
              install_requires=['requests'],
              )

if __name__=='__main__':
        main()