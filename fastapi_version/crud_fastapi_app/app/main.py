from typing import Optional
from datetime import datetime, date

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from sqlmodel import create_engine, Session, text, select, Field, SQLModel
from sqlalchemy import inspect
 
app = FastAPI()

engine = create_engine("sqlite:///../db.sqlite3")


# Разобраться как работает этот кусок кода. Конкретно этот класс.
class TechsupportProblem(SQLModel, table=True):
    __tablename__ = "techsupport_problem"
    
    id_request: Optional[int] = Field(default=None, primary_key=True)
    request_from_date: date
    name_of_problem: str
    description_of_problem: Optional[str] = None
    status: str = "Открыта"
    date_of_finish: Optional[date] = None
    user_id: int
    
    
# TODO Сделать стартовую страницу
@app.get("/")
def read_root():
    html_content = "<h2>Hello, world!</h2>"
    return HTMLResponse(content=html_content)


@app.get("/new_page")
def read_new_root():
    html_content = "<h2>Теперь я могу создавать маршруты!)</h2>"
    return HTMLResponse(content=html_content)

# TODO RBAC (Role-Based Access Control) — управление доступом на основе ролей
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
        
@app.get("/techsupport_problem")
def get_list_of_problems():
    table_name = "techsupport_problem"
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
    
# Тут тоже много вопросов. Надо почитать документацию
@app.get("/api/problems", response_model=list[TechsupportProblem])
def list_problem():
    with Session(engine) as s:
        return s.exec(select(TechsupportProblem)).all()
    
@app.get("/problems")
def problems_page():
    return FileResponse("static/problems.html")
# 1) Получить список заявок
# 2) сделать просмотр списка заявок
# 3) Сделать добавление заявок
# 4) Удаление заявок
# 5) Изменение заявок