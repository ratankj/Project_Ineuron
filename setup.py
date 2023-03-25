from setuptools import setup,find_packages

setup(name="cansus_income",
      version = "0.0.1",
      author="Ratan",
      author_email="imratankj@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )