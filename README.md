<p align="center" >
<div align="center" >
<img src="https://github.com/waseemofficial/DSA_Python/blob/main/Images/github_logo_blue.png"/>

</div>

<div align="center">
<a href="https://github.com/waseemofficial">
<img src="https://img.shields.io/badge/syed-waseem-93b023?&style=for-the-badge&logo=&logoColor=white"/></a>
<img src="https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white"/>
<img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
<img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
<img src="https://img.shields.io/badge/code%20style-black-000000.svg"/>


</div></p>


<div align="center">
<img src="https://img.shields.io/github/license/waseemofficial/{env.}.svg?style=flat"/> <img src="https://img.shields.io/github/stars/waseemofficial/{env.}.svg?colorB=orange&style=flat"/> <img sec="https://img.shields.io/github/languages/top/waseemofficial/{env.}.svg?style=flat"/> <img src="https://img.shields.io/github/languages/code-size/waseemofficial/{env.}.svg?style=flat"/> <img src="https://img.shields.io/github/issues-raw/waseemofficial/{env.}.svg?style=flat" />
</div>

<div align="center"> 

### Languages

![Python](https://img.shields.io/badge/-Python-000?&logo=Python)
![Bash](https://img.shields.io/badge/-Bash-000?&logo=gnu-bash&logoColor=white)
![Bash](https://img.shields.io/badge/-markdown-000?&logo=markdown)



### Technologies

![Linux](https://img.shields.io/badge/-Linux-000?&logo=Linux)
![GitHub](https://img.shields.io/badge/-GitHub-000?&logo=GitHub)
</div>
<div align="left">
 
# CLI Using Click 

</div>

### Setup
```py
from setuptools import setup, find_packages
setup(
    name="my_first_cli",
    version="0.0.1",
    py_modules=["main"],
    include_requires=["click"],
    entry_points={"console_scripts": ["cli=CLI.main:main_cli"]},
)

```

#### Using VHS for gif Recording

### instalarion 

> `scoop install vhs`

### for recording

> `vhs new <fileName>.tape`


using setup tools we can create a cli tool.
`pip install --editable .`

## Logging
`cli logging`

<img src="https://github.com/waseemofficial/CLI-using-Click/blob/main/CLI/Recordings/logging.gif" width="1000" height="800"/>

## Table
`cli table`

<img src="https://github.com/waseemofficial/CLI-using-Click/blob/main/CLI/Recordings/table.gif" width="1000" height="800"/>
## CSV file viewer
`cli viewers csv ./data/population.csv --has-header -n 10 --format github`

## convert CSV to JSON
`cli converters csv -i ./data/population.csv -o ./data/test.json --has-headers --columns country -c code -c Y2020 -c Y2021`

## View JSON file 
`cli viewers json ./data/test.json -n 25`