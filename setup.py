from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_teste3",
    version="0.0.3",
    author="Carlos",
    author_email="calex_matrix@hotmail.com",
    description="Versão de teste DIO - Processamento de imagem. Este projeto pertence a Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist na Take. O pacote é uma demonstração para simulação de upload no site Test Pypi, e é da classe do desenvolvedor do Bootcamp . E-mail: karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)