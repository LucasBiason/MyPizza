# My Pizza

This project is a register of pizzerias accredited by the Quality Control program. MyDinnerTour.

The API manages pizzerias, owners and the establishment's menu.

The system is made with Django with a database in Postgresql, with the option of running it through Docker.

This project can be used as a knowledge meter

API documentation is available via Postman in the docs folder.

### Installing via virtual environment

We use Pyenv to build the environments, after installation, you can install the version of python used in this project with the command:

```bash
pyenv install 3.8.5
```

After that it will be necessary to activate the installation

```bash
pyenv shell 3.8.5
```

Now create the environment with the command

```bash
pyenv virtualenv mypizza-env
```

Once created, we can activate with the command:

```bash
pyenv activate mypizza-env
```

After activation, install the required libraries in the linux-requirements.sh and requirements.txt files:

```bash
sudo apt-get update && bash linux-requirements.sh

pip install pip setuptools --no-cache-dir

pip install -r requirements.txt --no-cache-dir
```

Your project will need in the environment variables. Create a .env file in tizza / with the environment variables according to the .env.sample model.
After that it can be executed:

```bash
# Start the bank migration
python src/manage.py migrate

# Create a superuser to use the application
python src/manage.py createsuperuser
<< Follow the creation instructions >>

# Now it can be executed
python src/manage.py runserver 0.0.0.0/16000

```

### Running by Docker

To use docker you can run the docker compose available using:

```bash
docker-compose build
docker-compose up
```
