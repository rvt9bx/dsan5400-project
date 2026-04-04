import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='recipe_simplifier',
    version='0.0.1',
    author='Eleanor Byrd',
    author_email='eb1481@georgetown.edu',
    description='Simplifies Recipe Text ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    extras_requres={"dev": ["pytest", "flake8", "autopep8"]},
    )