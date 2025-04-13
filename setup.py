from setuptools import setup, find_packages

setup(
    name="stock-trends",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "yfinance",
        "PyYAML",
        "scipy",
    ],
    entry_points={
        "console_scripts": [
            "process-ticker-yaml=stock_trends.scripts.process_ticker_yaml:main",
            "allocate-portfolio=stock_trends.scripts.allocate_portfolio:main",
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