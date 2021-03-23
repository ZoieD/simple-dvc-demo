conda create env -
```bash
conda create -n wineq python=3.7
```
`conda activate wineq`

create a req file and install 
`pip install -r requirements.txt`

download the data from 
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

git init
`git init`

dvc init
`dvc init`

dvc add datasets
`dvc add data_given/winequality.csv`

git add changes and first commit
`git add .`
`git commit -m "first commit"`

update readme and git commit
`git add .`
`git commit -m "update README.md"`

git push to remote repo
`git remote add origin https://github.com/dorisdouzi/simple-dvc-demo.git`
`git branch -M main`
`git push -u origin main`


`dvc repro`
`dvc params diff`
`dvc metrics show`
`dvc metrics diff`

tox command
`tox`
rebuilding the envs
`tox -r`

pytest command
`pytest -v`

setup command (setup.py)
`pip install -e .`
check current packages
`pip freeze`
build your own package commands
`python setup.py sdist bdist_wheel`










