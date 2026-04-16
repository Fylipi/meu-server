from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

ADMIN_USER = os.getenv("ADMIN_WEB_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_WEB_PASS", "admin123")

@app.get("/")
async def root():
    return RedirectResponse(url="/admin/login", status_code=302)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/admin/login", response_class=HTMLResponse)
async def admin_login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
    )

@app.post("/admin/login", response_class=HTMLResponse)
async def admin_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USER and password == ADMIN_PASS:
        return RedirectResponse(url="/admin", status_code=302)

    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request, "error": "Login inválido"},
        status_code=401
    )

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse(
        request,
        "admin.html",
        {"request": request}
    )
