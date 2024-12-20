from fastapi import FastAPI
from routes import router as translation_router

app = FastAPI()


app = FastAPI(title="Banglish to Bangla API")
app.include_router(translation_router)
@app.get('/')
def root():
    return {"message": "welcome to banglish to bangla api"}