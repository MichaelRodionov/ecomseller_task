# Test task for Ecomseller company
___
## Tech stack:
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>     
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi"/>
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/celery-%23316192.svg?style=for-the-badge&logo=celery&logoColor=white"/>
<img src="https://img.shields.io/badge/alembic-%234DC730.svg?style=for-the-badge&logo=alembic&logoColor=white"/>   

___
## This application consists of:   
- API interface
### API features:
- Endpoint input receives data for authorization in Ozon-seller service;
- Request for ozon-seller by Ozon API interface;
- Get result of request and send it to celery task;
- If the result is not in the database, it will be written. This prevents duplicates from appearing in the database.
___
### Project structure
- `migrations/` : package with db migrations
- `src/config/` : package with app and celery config
- `src/core/` : package with app core
- `src/models/` : package with models
- `src/structures/` : package with pydantic structure
- `src/tasks/` : package with celery tasks
- `src/main.py` : app start file
- `src/worker.py` : celery worker file
- `alembic.ini` : alembic configuration
- `poetry.toml` : file to install dependencies with poetry
- `requirements.txt` : file to install dependencies with pip

___
### Local start
1) Clone repository
``` python
git clone https://github.com/MichaelRodionov/ecomseller_task.git
```
2) Create your own repository   
3) Add remote to your GitHub repository by repository URL   
4) Push code to your repository
``` python
git add .  # add all files to Git
git commit -m 'add project'  # initial commit
git push  # push to repository
```
4) Create and activate virtual environment   
5) Create local `.env` file with the next data:  
``` python
DB_USER = 'your db user'
DB_PASSWORD = 'your db password'
DB_HOST = 'your db host'
DB_PORT = 'your db port'
DB_NAME = 'your db name'
CELERY_BROKER_URL = 'your broker url' # redis://localhost:6379/0
CELERY_RESULT_BACKEND = 'your result backend url' # redis://localhost:6379/1
```
6) Start redis
``` python
docker run -d -p 6379:6379 --name redis redis 
```
7) Open the first terminal window and navigate to the root of the project. Start celery worker.   
``` python
celery -A src.tasks.db_write:celery worker --loglevel=info  
```
8) Open the second terminal window and navigate to the root of the project. Start celery flower.   
``` python
celery -A src.tasks.db_write:celery flower
# Now you can follow all celery tasks and workers by the address http://localhost:5555   
``` 
9) Start application in your IDE
``` python
uvicorn src.main:app --host 0.0.0.0 --port 8000 
```
___
### API requests are available on address http://localhost:8000
``` python
# Endpoint is available by route
/api/v1/result/{<offer_id>}
```