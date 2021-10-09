from fastapi import FastAPI

from routers import stub

app = FastAPI()

app.include_router(stub.router)