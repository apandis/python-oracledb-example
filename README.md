# Oracle DB Connection Project

A minimal Python project that demonstrates how to connect to an Oracle database using the `python-oracledb` driver.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/apandis/python-oracledb-example.git
   cd python-oracledb-exampl
   ```


2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   ```

   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root with the following content:

   ```ini
   DB_USER=your_username
   DB_PASS=your_password
   DB_SERVER=your_server_address
   DB_PORT=1521
   DB_SERVICE=your_service_name
   ```

## Running the Application

To connect to the Oracle database and execute a sample query, run:

```bash
python src/main.py
```

## Running Tests

To run the tests, use:

```bash
python -m unittest discover tests
```

## Dependencies

- [python-oracledb](https://oracle.github.io/python-oracledb/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
