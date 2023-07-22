from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pyngrok import ngrok
import uvicorn
import nest_asyncio
from fastapi.responses import StreamingResponse
import requests


app = FastAPI()


@app.get("/load_file")
def load_file(file_url: str):
    response = requests.get(file_url)
    if response.status_code == 200:
      return StreamingResponse(response.iter_content(chunk_size=1024), media_type="application/octet-stream")
    else:
      return {"error": "Failed to retrieve file"}


@app.get("/load_file_length")
def load_file(file_url: str):
    response = requests.head(file_url)  # Send a HEAD request to get only the headers
    if response.status_code == 200:
        content_length = response.headers.get('Content-Length')
        return {"content_length": content_length}
   


@app.get("/load_file_name")
def load_file(file_url: str):
    filename = file_url.split("/")[-1]  # Extract filename from the URL
    return {"filename": filename}


# ngrok.set_auth_token("2RnhHsTNA7aSE5aLRBogzVxPmDd_5MUj2ckcUMZcJ1786CRs3")
# # Connect Ngrok to the same port as the Uvicorn server
# ngrok_tunnel = ngrok.connect(8000)
# print('Public URL:', ngrok_tunnel.public_url)
# nest_asyncio.apply()
# uvicorn.run(app, port=8000)
