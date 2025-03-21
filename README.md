# О проекте  
Этот репозиторий создан в демонстрационных целях, в рамках курса *Data Analysis* от [aiacademy.tj](aiacademy.tj).  

# Цель проекта  
Познакомить студентов с процессом создания интерактивных аналитических дашбордов.

# Использованные источники данных  
Для проекта использовался набор данных ["Adventure Works"](https://mattallington.com.au/wp-content/uploads/2023/10/AdventureWorks.zip) — вымышленной базы данных от Microsoft, которая часто применяется для демонстрации возможностей анализа данных, построения отчетов и разработки бизнес-решений.  

# Структура репозитория

*   `queries/`: Содержит SQL запросы для работы с базой данных.
*   `source/`: Содержит исходные данные для импорта в базу данных.
*   `.gitignore`: Файл, указывающий, какие файлы и папки следует игнорировать при отслеживании изменений в Git.
*   `customers.py`: Python скрипт для создания страницы дашборда `Customer base analysis`.
*   `sales.py`: Python скрипт для создания страницы дашборда о продажах (ещё в разработке).
*   `db.py`: Python скрипт, содержащий функции для чтения данных из БД.
*   `ddl.py`: Python скрипт для создания структуры базы данных и заполнения таблиц.
*   `main.py`: Основной скрипт, запускающий приложение.
*   `my.db`: Файл базы данных DuckDB.
*   `requirements.txt`: Файл, содержащий список необходимых Python пакетов.
*   `tables.json`: JSON файл, содержащий метаданные о таблицах в базе данных.

# Использованные библиотеки  
* duckdb==1.2.1
* openpyxl==3.1.5
* pandas==2.2.3
* plotly==6.0.0
* streamlit==1.43.2

# Деплой  
Дашборд задеплоен на платформе *Streamlit Cloud* и доступен по следующей ссылке: https://datacoach2024-adventure-works-main-d7cqxx.streamlit.app/
