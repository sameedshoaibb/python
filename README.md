# python
War with Python has started

#To create a python virtual environment

#Create a python virtual environment
virtualenv .docker
# Enable the virtual environment
source .docker/bin/activate

# To disable virtual env
deactivate

# To check dependencies
pip list

#The path which we are using will display
which python

#TO locate all the dependencies in the requirement.txt file
pip freeze > requirements.txt

# To use the requirements.txt
pip install -r requirements.txt

#To create virtual_env of a specific python version
virtualenv -p /usr/bin/python2.7 pymongo_env
source pymongo_env/bin/activate
python --version

