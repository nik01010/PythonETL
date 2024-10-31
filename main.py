# ReadMe --------------------------------------------------------------------------
# Main file for the PythonETL project

# Packages ------------------------------------------------------------------------
from pyBuildReleaseTest.Helpers.Logger import initialise_logger
from pyBuildReleaseTest.DataAccess.ApplicationDbContext import ApplicationDbContext, ConnectionDetails
from pyBuildReleaseTest.DataAccess.PersonService import PersonService
from pyBuildReleaseTest.DataModel.Person import Person
from configparser import ConfigParser
from logging import Logger
from pandas import DataFrame


def main():
    # Configuration ---------------------------------------------------------------
    app_config_filepath: str = "./config/app_config.yaml"
    app_config: ConfigParser = ConfigParser()
    app_config.read(app_config_filepath)

    log_file_path: str = app_config.get("logger", "log_file_path")
    logger: Logger = initialise_logger(file_path = log_file_path)

    logger.info("Starting ETL Process")


    # Connect ---------------------------------------------------------------------
    logger.info("Connecting to Database")
    connection_details: ConnectionDetails = ConnectionDetails(
        server = app_config.get("connection", "server"),
        database = app_config.get("connection", "database"),
        driver = app_config.get("connection", "driver")
    )
    connection_string: str = connection_details.get_connection_string()

    database_context: ApplicationDbContext = ApplicationDbContext(connection_string = connection_string)

    person_service: PersonService = PersonService(database_context = database_context)


    # Read ------------------------------------------------------------------------
    logger.info("Extracting Data")
    people_count: int = person_service.get_people_count()

    people: DataFrame = person_service.get_people()

    person_by_id: Person = person_service.get_person(id = 16003)

    people_bob: DataFrame = person_service.get_people_by_name(first_name = "Bob")
    people_chapman: DataFrame = person_service.get_people_by_name(last_name = "Chapman")
    people_bob_chapman: DataFrame = person_service.get_people_by_name(first_name = "Bob", last_name = "Chapman")


    # Create ----------------------------------------------------------------------
    logger.info("Creating Data")
    new_person: Person = Person(
        PersonType = "EM", NameStyle = 0, Title = "Mr", FirstName = "Tom", LastName = "Jerry", EmailPromotion = 1
    )
    new_person_id: int = person_service.create_person(new_person = new_person)


    # Edit ------------------------------------------------------------------------
    logger.info("Editing Data")
    edited_person: Person = new_person
    edited_person.MiddleName = "Anderson"
    person_service.edit_person(id = new_person_id, edited_person = edited_person)
    

    # Delete ----------------------------------------------------------------------
    logger.info("Deleting Data")
    deleted_records: int = person_service.delete_person(id = new_person_id)


    # Disconnect ------------------------------------------------------------------
    database_context.disconnect()

    logger.info("ETL Process completed")

if __name__ == '__main__':
    main()
