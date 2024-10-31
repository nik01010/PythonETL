# PythonETL

Proof of concept Python project to explore ETL best practice

## Dependencies
This project is an extension of the package [pyBuildReleaseTest](https://github.com/nik01010/pyBuildReleaseTest)

## Install requirements
- pip install -r requirements.txt

## Usage

- See the file [main.py](main.py)

## Maintenance

### Configuration
- Configurations are stored in [app_config.yaml](./config/app_config.yaml)

### Update requirements
- pip install pipreqs
- pipreqs ./


## Example Logs
```log
[2024-10-31 15:25:40] [DEBUG] [Logger.py] [initialise_logger] [29] Logging configured using level: DEBUG
[2024-10-31 15:25:40] [DEBUG] [Logger.py] [initialise_logger] [32] Logging to file path: test_log.log
[2024-10-31 15:25:40] [INFO] [main.py] [main] [23] Starting ETL Process
[2024-10-31 15:25:40] [INFO] [main.py] [main] [26] Connecting to Database
[2024-10-31 15:25:40] [DEBUG] [ApplicationDbContext.py] [__init__] [21] Database context using connection string: mssql+pyodbc://localhost/AdventureWorks2022?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server
[2024-10-31 15:25:40] [DEBUG] [ApplicationDbContext.py] [__init__] [28] Created database connection
[2024-10-31 15:25:40] [INFO] [main.py] [main] [40] Extracting Data
[2024-10-31 15:25:41] [INFO] [main.py] [main] [53] Creating Data
[2024-10-31 15:25:41] [DEBUG] [PersonService.py] [create_person] [71] Created new Person with BusinessEntityID: 20821
[2024-10-31 15:25:41] [INFO] [main.py] [main] [61] Editing Data
[2024-10-31 15:25:41] [DEBUG] [PersonService.py] [edit_person] [86] Edited Person with BusinessEntityID: 20821
[2024-10-31 15:25:41] [INFO] [main.py] [main] [68] Deleting Data
[2024-10-31 15:25:41] [DEBUG] [PersonService.py] [delete_person] [104] Deleted 1 records for Person with BusinessEntityID: 20821
[2024-10-31 15:25:41] [INFO] [main.py] [main] [75] ETL Process completed
```
