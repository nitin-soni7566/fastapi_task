# FastAPI Project

This project is a FastAPI application that demonstrates how to set up and run a FastAPI server with SQLAlchemy and Pydantic for ORM and data validation.

## Task

### Local Development Steps 

1. **Install Poetry (In project directory)**:
    ```sh
    pip install poetry
    ```

2. **Activate the Poetry Shell**:
    ```sh
    poetry shell
    ```

3. **Install Dependencies**:
    ```sh
    poetry install
    ```

4. **Run the Application**:
    ```sh
    uvicorn src.main:app --reload
    ```

5. **Access the API Documentation**:
    - Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs).
