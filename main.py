from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/health")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/login", response_class=HTMLResponse)
def login():
    return """
    <html>
      <body>
        <h1>Login</h1>
        <p>Servidor funcionando.</p>
      </body>
    </html>
    """

@app.get("/admin", response_class=HTMLResponse)
def admin():
    return """
    <html>
      <body>
        <h1>Admin</h1>
        <p>Painel admin online.</p>
      </body>
    </html>
    """
