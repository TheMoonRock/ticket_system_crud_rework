from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlmodel import create_engine, Session, text
from sqlalchemy import inspect
 
app = FastAPI()

engine = create_engine("sqlite:///../db.sqlite3")

# Сделать стартовую страницу
@app.get("/")
def read_root():
    html_content = "<h2>Hello, world!</h2>"
    return HTMLResponse(content=html_content)


@app.get("/new_page")
def read_new_root():
    html_content = "<h2>Теперь я могу создавать маршруты!)</h2>"
    return HTMLResponse(content=html_content)

# RBAC (Role-Based Access Control) — управление доступом на основе ролей
@app.get("/db/tables")
def get_tables():
    inspector = inspect(engine)
    return {"tables:": inspector.get_table_names()}

@app.get("/db/tables/{table_name}")
def get_table_data(table_name: str):
    with Session(engine) as session:
        try:
            result = session.exec(text(f"SELECT * FROM {table_name}"))
            
            columns = result.keys()
            data = [dict(zip(columns, row)) for row in result.fetchall()]
            
            return {
                "table": table_name,
                "count": len(data),
                "rows": data
            }
        except Exception as e:
            return {"error": f"Не удалось прочитать таблицу. Ошибка: {str(e)}"}