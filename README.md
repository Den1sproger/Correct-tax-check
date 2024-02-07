# Correct-tax-check
Test task on checking on the correctness of taxes. This is a web application with which the user can send a file with the source data and in response receive a generated report based on the source data.

## Start

Clone this repository
```
git clone https://github.com/Den1sproger/Correct-tax-check.git

```

Create Django Secret Key [here](https://djecrety.ir/).

Paste secret key to the: **correct_tax/environ/.env**

1. Create virtual environment

Windows
```
python -m venv venv
```

Mac/Linux
```
python3 -m venv venv
```

2. Enable virtual environment

Windows
```
venv/Scripts/Activate.ps1
```

Mac/Linux
```
source venv/bin/activate
```

3. Install dependencies
```
pip install -r correct_tax/requirements.txt
```
### Method without makefile
***
3. Change project directory
```
cd correct_tax
```
4. Collect static files

Windows
```
python manage.py collectstatic --no-input
```
Mac/Linux
```
python3 manage.py collectstatic --no-input
```
5. Run server

Windows
```
python manage.py runserver
```
Mac/Linux
```
python3 manage.py runserver
```
### Method via makefile
***
3. Collect static files
```
make static
```
4. Run server
```
make run
```


## Start via Docker

1. Change project directory
```
cd correct_tax
```

2. Create Docker image
```
docker compose build
```

3. Run Docker containers
```
docker compose up
```


## Using guide
1. Select the excel file by clicking on the "choose file" button
2. Click on the "Submit" button
3. Download the generated report from the received link