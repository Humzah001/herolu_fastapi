from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import requests


app = FastAPI()


@app.get("/")
def load_file(file_url: str):
    return{"Hello World"}
    
