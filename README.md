# fast-api-practice

# Description
This is the fast-api practice. This domain is used for:
    - Small structured project using fastApi.
    - Using SqlAlchemy core to interact with Database basic CRUD operations
    - Using Service layer to access DB, and API layer to implement the endpoints
    - Pydantic models as a serializer
    - Error handlers to be handled automatically

### Sandbox setup
1. Clone this repository and navigate to it
2. Create a virtualenv 
    ```
    pip3 install virtualenv
    virtualenv venv
    ```
3. Activate virtualenv
    ```
    source venv/bin/activate
    ```
4. Install dependencies
    ```
    pip3 install -r requirements-dev.txt
    ```
5. You have to install PostgreSql on your machine and edit the connection string and the alembic.ini file as per the DB setup

6. run the migration file from alembic so you can use database after it being created
    ```
    alembic upgrade head
    ```

7. Attempt to start the webserver
   ```
   uvicorn application:app --reload
   ```
OR
### Using docker which is mostly preferred
1. Clone this repository and navigate to it

2. install docker on your machine in case windows OS use the link below
    ```
    https://docs.docker.com/docker-for-windows/install/
    ```
    or just use this link to install virtual machine Ubuntu OS and run app there then install docker and go ahead
    ```
    https://www.thomasmaurer.ch/2019/06/how-to-create-an-ubuntu-vm-on-windows-10/
    ```
