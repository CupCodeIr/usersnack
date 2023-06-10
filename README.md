
# Usersnack

A python backend web application created with FastAPI


## Deployment

- Create and activate a virtual environment and install the required packages mentioned in requirements.txt using pip 

```bash
  pip install requirements.txt
```

Using a webserver like `Uvicorn` run the main.py file from the project root directory as an application

```bash 

python -m uvicorn main:app
```


## Create And Seed The Tables

In order to create and seed the tables with sample data you can simply run the seed.py file in root project directory

```bash
python seed.py
```
