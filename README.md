# Notes_API

| Endpoint           | Parameters                                                                                                  |
|--------------------|-------------------------------------------------------------------------------------------------------------|
| GET /users/{email} | **request body** <br> *email*: string                                                                       |
| GET /users         | **None**                                                                                                    |
| GET /usersme       | **None**                                                                                                    |
 | POST /users        | **request body**<br> *email*: string<br>*first_name*: string<br/>*last_name*: string<br/>*password*: string |  
 | POST /users/token  | **request body**<br> *email*: string<br>*password*: string                                                  |  
 | POST /notes        | **request body**<br/>*text*: string                                                                         |  
 | GET /notes         | **None**                                                                                                    |  
| PUT /notes         | **request body**<br/>*text*: string<br/>*id*: int                                                           |  
| DELETE /notes      | **request body**<br/>*id*: int                                                                              |  
 

### Локальный запуск
Для локального запуска используйте: `main.py`

### Версии

*fastapi version 0.78.0*

*SQLAlchemy version 1.4.37*

*Python 3.10.2*