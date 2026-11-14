from fastapi import FastAPI

import uvicorn

app=FastAPI()

@app.get("/health")
def healthStatus():
    return {"Status":"Ok"}



if __name__ == "__main__":
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)
