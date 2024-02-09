# Pivot Traffic


## Installation
`python setup.py install`
## To Run
```
$ pivottraffic --help
usage: pivottraffic [-h] baseurl outputfile

Aggregate and pivot traffic data files found at X base url.

positional arguments:
  baseurl     Base URL location of files to download
  outputfile  Output file for formatted csv

options:
  -h, --help  show this help message and exit

```

## Requirements
* Python >= 3
* pandas >= 2.2.0



## TODO
* add tests
* add basic python logging and better exception handling