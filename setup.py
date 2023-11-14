from setuptools import setup, find_packages

# pip install setuptools wheel
# python setup.py sdist bdist_wheel
# pip install twine
# pip install --upgrade pip setuptools twine
# twine upload dist/*



setup(
    name='my-package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # لیست وابستگی‌های اصلی
        'requests',
        'numpy',
    ],
    extras_require={
        'all': [
            # وابستگی‌های مربوط به گروه all
            'matplotlib',
            'scipy',
        ],
        'minimum': [
            # وابستگی‌های مربوط به گروه minimum
            'flask',
        ],
    },
    entry_points={
        'console_scripts': [
            'my-command = my_package.module1:main_function',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)