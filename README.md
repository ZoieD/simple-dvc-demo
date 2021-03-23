<<<<<<< HEAD
conda create env
=======
conda create env -
>>>>>>> 3d8f21d93544949567ee99bd59474ac25dab3dd4
```bash
conda create -n wineq python=3.7
```
```bash
conda activate wineq
```

create a req file and install 
```bash
pip install -r requirements.txt
```

download the data from 
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

git init
```bash
git init
```

dvc init
```bash
dvc init
```

dvc add datasets
```bash
dvc add data_given/winequality.cs
```

git add changes and first commit
```bash 
git add .
git commit -m "first commit"
```

update readme and git commit
```bash
git add .
git commit -m "update README.md"
```

git push to remote repo
```bash
git remote add origin https://github.com/dorisdouzi/simple-dvc-demo.git
git branch -M main
git push -u origin main
```

dvc commands
```bash
dvc repro
dvc params diff
dvc metrics show
dvc metrics diff
```

tox command
```bash
tox
```
rebuilding the envs
<<<<<<< HEAD
```bash
=======
```bash
>>>>>>> 3d8f21d93544949567ee99bd59474ac25dab3dd4
tox -r
```

pytest command
```bash
pytest -v
```

setup command (setup.py)
```bash
pip install -e .
check current packages
pip freez
````
build your own package commands
```bash
python setup.py sdist bdist_wheel
```
<<<<<<< HEAD
=======










>>>>>>> 3d8f21d93544949567ee99bd59474ac25dab3dd4
