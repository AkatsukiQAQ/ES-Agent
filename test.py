from fastapi import FastAPI

app = FastAPI()

print("正在运行 test.py")

@app.get("/")
async def root():
    return {"message": "Hello World"}