# Tankonstin Forum

Simple web application project to boost Python skills and to investigate the
specifics of Django-driven apps.

## How to run on localhost (Windows)

1. Roll out the virtual environment and install the required dependencies:
```
python -m venv env
.\env\Scripts\activate
python -m pip install -r requirements.txt
```

2. Set up `forumDB` database on local PostgreSQL DBMS instance:
```sql
CREATE DATABASE "forumDB"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
```

3. Create `forumuser` login role with password `<your_password>` and set it as
"Owner" for `forumDB`:
```sql
CREATE ROLE forumuser WITH
    LOGIN
    NOSUPERUSER
    INHERIT
    CREATEDB
    NOCREATEROLE
    NOREPLICATION
    ENCRYPTED PASSWORD '<hash>';
```

4. Create `settings.json` in the project root directory. The contents are:
```json
{
    "DB_PASSWORD": "<your_password>",
    "SECRET_KEY": "somewhatincrediblysecurestring"
}
```
5. Apply migrations:
```
python manage.py migrate
```

6. Run the web application:
```
python manage.py runserver
```
The following (or similar) log messages must be displayed if everything went OK:
```
Performing system checks...

System check identified no issues (0 silenced).
December 25, 2021 - 05:56:19
Django version 2.1.4, using settings 'sample.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Suggestions, bugs, whatever

Please feel free to post your thoughts about potential improvements, bug
reports, any kind of comments in the
[Issues](https://github.com/kostmetallist/tankonstin-forum/issues) section.
