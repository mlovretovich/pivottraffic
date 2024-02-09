# Pivot Traffic

Write a program that converts the web traffic from these 26 CSV files into a single CSV file that
contains one row for each user_id and has columns populated with the length of time each user
spent on each path.

## Installation
`python setup.py install`
## To Run
```
$ pivottraffic --help
usage: pivottraffic [-h] baseurl outputfile

Aggregate and pivot traffic data files found at X base url.

positional arguments:
  baseurl     Base URL or directory location of files to download: http://test.com/dir/
  outputfile  Output file for formatted csv

options:
  -h, --help  show this help message and exit

```

## Example
`$ pivottraffic https://public.wiwdata.com/engineering-challenge/data/ output.csv`

## Requirements
* Python >= 3
* pandas == 2.2.0



## TODO
* add tests for transformation code
* add basic python logging and better exception handling