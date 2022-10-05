[![Test](https://github.com/rohitgeddam/CSC510_HW1/actions/workflows/build.yml/badge.svg)](https://github.com/rohitgeddam/CSC510_HW1/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Arun152k/CSC510_HW1/branch/HW1/graph/badge.svg?token=WA4KNGKU6J)](https://codecov.io/gh/Arun152k/CSC510_HW1)
[![code_size](https://img.shields.io/github/languages/code-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1) 
[![repo_size](https://img.shields.io/github/repo-size/rohitgeddam/CSC510_PROJECT1)](https://github.com/rohitgeddam/CSC510_PROJECT1)</br>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7061868.svg)](https://doi.org/10.5281/zenodo.7061868)

# FindMyRoomie 👯‍♂️

### How to setup the project on your local machine?
* `git clone https://github.com/rohitgeddam/CSC510_PROJECT1.git`
* Setup virtual environment
  * `python -m venv venv`
  * On Mac/Linux
    * `source venv/bin/activate`
  * On Windows
    * `venv\Scripts\activate`
* `pip install -r requirements.txt`
* `cd src`
* `python manage.py runserver`
* `python manage.py migrate`


## Populate fake data for testing

```
python manage.py shell

>>> from django.contrib.auth.models import User
>>> from django_seed import Seed
>>> seeder = Seed.seeder()
>>> seeder.add_entity(User)
```
