from setuptools import find_packages, setup

setup(
    name="my-test-ify",
    version="0.0.2",
    description="Micro framework de testes unitários minimalista",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Andre Luiz",
    author_email="andrebg28@gmail.com",
    url="https://github.com/andrebg28/my-test-ify.git",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=[],  # Este projeto não tem dependências externas
    extras_require={
        "dev": [
            # Dependências de desenvolvimento
            "flake8>=7.1.1",
            "black>=24.1",
            "mypy>=1.13.0",
        ]
    },
)
