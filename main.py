from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Login Page</title>
        </head>
        <body>
            <h1>Login</h1>
            <form action="/login/" method="post">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Login" id="login">
            </form>
        </body>
    </html>
    """

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "validUser" and password == "validPass":
        return {"message": "Login successful!"}
    else:
        return {"message": "Login failed!"}