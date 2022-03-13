from fastapi import FastAPI, Response
from pydantic import BaseModel
import subprocess
import tempfile
import json






app = FastAPI()


class Scan(BaseModel):
    target: str


@app.post("/scans")
def create_scan(scan: Scan, response: Response):
    with tempfile.NamedTemporaryFile() as file:
        process = subprocess.run(
            ["testssl", "--jsonfile", file.name, scan.target])

        response.status_code = 201
        return json.load(file)
