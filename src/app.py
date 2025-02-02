from fastapi import FastAPI

from auth.routes import router as auth_routes
from examples.routes import router as example_routes
from users.routes import router as users_routes

app = FastAPI(title="Beyond CRUD 2")
app.include_router(auth_routes)
app.include_router(example_routes)
app.include_router(users_routes)
