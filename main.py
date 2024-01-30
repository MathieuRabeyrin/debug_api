from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/api/status-code/{status_code}")
async def root(status_code: int, response: Response):
    response.status_code = status_code
    return status_code
