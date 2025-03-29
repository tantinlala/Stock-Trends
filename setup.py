from setuptools import setup, find_packages

setup(
    name="stock-trends",
    version="0.1.0",
    packages=['stock_trends'],
    install_requires=[
        "pandas",
        "matplotlib",
        "yfinance",
    ],
    entry_points={
        "console_scripts": [
            "compare-ticker=stock_trends.scripts.compare_ticker:main",
        ],
    },
    author="Nicholas",
    description="A package to compare stock trends with the S&P 500.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)