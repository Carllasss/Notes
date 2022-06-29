from fastapi import FastAPI

from routers import notes_routes, user_routes


app = FastAPI(openapi_url='/openapi.json')

app.router.prefix = '/api/v1'

app.include_router(user_routes, prefix='/users')
app.include_router(notes_routes, prefix='/notes')