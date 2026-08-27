from fastapi import FastAPI
from customerapi import router
from databasefastapi import create_table

app = FastAPI()

create_table()

app.include_router(router)
