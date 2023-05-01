# !/bin/bash

<<com
Create Project
com

function create_project()
{
    django-admin startproject django_poll
    cd django_poll/
    pip freeze > requirements.txt
}


function run_poject()
{
    python manage.py migrate
    python manage.py runserver
}

<<com 
create env 
com

read -p "Eneter your perfer venv name : " venv_name

if [[ $venv_name == "" ]]
then
    venv_name="venv"
fi

echo "${venv_name} creation starting...."

python3 -m venv $venv_name

echo "${venv_name} created"


<<com
activate your env
com

echo "activating ${venv_name} ....."

source ${venv_name}/bin/activate

echo "${venv_name} activate"


<<com
Clone Project from Github
com

echo "Trying to clone from Git"

# if private add ssh before clone
git clone https://github.com/do-community/django-polls.git

echo "clone completed"


<<com
Enter into folder
com

echo "Entering into project folder"

if [ -d "django_poll" ]
then
    cd django-poll/
    export PROJECT_DB_NAME='MyDB'
    export PROJECT_DB_PORT='5432'
fi


<<com
Install required
com

echo "Installing dependency"

if [ -f "requirements.txt" ]
then
    echo "Found Project"
    pip install -r requirements.txt
else
    echo "creating new project"
    pip install django numpy pandas requests
    create_project
fi

<<com 
Run project
com

run_poject
