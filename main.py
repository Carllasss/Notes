from fastapi import FastAPI
import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware
from routers.notes_routes import note_router
from routers.user_routes import user_router


app = FastAPI(openapi_url='/openapi.json', debug=True)


app.include_router(user_router, prefix='/users')
app.include_router(note_router, prefix='/notes')

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url='postgresql://postgres:12345@localhost:5432/notes')

# To run locally
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)