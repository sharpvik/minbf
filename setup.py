from setuptools import setup

setup(
    name='minbf-brainf-minifier',
    version='0.1.0',
    author='Viktor A. Rozenko Voitenko',
    author_email='sharp.vik@gmail.com',
    description='MinBF is a tiny script that lets you minify your Brainf files by skipping all but essential characters in a file.',
    url='https://github.com/sharpvik/minbf',
    license='MIT',
    py_modules=['minbf'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        minbf=minbf:minify
    """,
)
