from fastapi import FastAPI
import uvicorn

app = FastAPI()


# Declare the first route- returns a simple JSON object on the index page
@app.get("/")
def index():
    '''
    This is a first docstring
    '''
    return {"message": "Hello,stranger!"}


# Declare the seconde route- returns a simple JSON object containing a personalized message
@app.get("/{name}")
def get_name(name: str):
    '''
    This is a second docstring
    '''
    return {"message": f"Hello, {name}"}


if __name__ == "__main__":
    uvicorn.run(app, port=8085)
