
# Currency Converter App with FastAPI

This is a simple backend project developed with Fast API. It scrapes the current currency rate according to https://wise.com/gb/currency-converter/


## Requirements
* Python3.10+
* FastAPI
* NoSql Database (MongoDB)


## Running the Server
Set your environment variables as parameters in `.env` file.

### STEP 1: Install Requirements.txt
Create a virtual enviroment and install packages in `requirements.txt`
```
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### STEP 2: Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ATLAS_URI`: Get [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/). Ensure you replace the username and password placeholders with your own credentials!

`DB_NAME`: Set the name of the database created.

`API_KEY`: Specify an API Key to authenticate requests

```
ATLAS_URI:"mongodb+srv://admin:<password>@cluster0.oc32b5z.mongodb.net/test"
DBNAME:"testDB"
APIKEY:"Jha8dJm8MPlQ2aBzoKJ03TuzJrRxTeMx9Xenb7"
```

### STEP 3: Start the Application
Start the server by running the command
```
uvicorn main:app --reload
```
only use the keyword `--reload` in development mode.

On the CLI, note the port Uvicorn is running on. By default, it runs on port `8000`.
```
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Documentation
FastAPI includes automatic interactive API documentations provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)
Visit
```
http://127.0.0.1:8000/docs
```
or
```
http://127.0.0.1:8000/redoc
```
to see documentation of the application\
Note: if you use a different port other than `8000`, replace it accordingly in the URL.


## Disclaimer
The application only scrapes information based on other sources. It does not claim to provide financial or investment advice.\
*USE AT YOUR OWN RISK*
