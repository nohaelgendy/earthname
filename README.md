# Earth Name Project

Website using Flask microframework.

## About

Website intiated for the memory of "Earth Day - 22 April". The current feature that the user can enter his/her kid name then get a pdf file containing a coloring drawing about the earth with his/her name.

## Setup

1. Install [python](https://www.python.org/downloads/) if you don't have it. 

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd earthname
   ```

4. Create a new virtual enviroment:

    *Note: When running the commands, you may need to type python3/pip3 instead of python/pip depending on your setup.*

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the dependencies (python pacakages) listed in "requirements.txt" file:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Create the enviroment variables file ".env":

   ```bash
   $ touch .env
   ```

7. Add this variables to the .env file:

   ```bash
    FLASK_APP=app
    FLASK_ENV=development
   ```

8. Run the app:

   ```bash
   $ flask run
   ```

## Links

* Flask Project Layout: https://flask.palletsprojects.com/en/2.2.x/tutorial/layout/

## Understand 

### Why '.env' file ?

We use .env to store environment variables for our application, which allows us to keep sensitive information, such as API keys and passwords, out of our codebase and hidden from others.

required library: --> python-dotenv