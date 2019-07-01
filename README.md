
Install and Configure Mongodb, using following steps :

1. Run "sudo vi /etc/yum.repos.d/mongodb.repo"

2. Copy and Paste following content :

	[Mongodb]
	name=MongoDB Repository
	baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/4.0/x86_64/
	gpgcheck=1
	enabled=1
	gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc



3. Run "sudo dnf install mongodb-org"

4. Run "sudo systemctl enable mongod.service"
5. Run "sudo systemctl start mongod.service"
6. Run "sudo systemctl status mongod.service"


---------------------------------------------
Install following Python requirements :

1. Run "pip install virtualenv flask Flask-API mongoengine pytest pytest-cov requests"

----------------------------------------------
Run the App, using Following commands :

1. Run "virtualenv book_manager_env"
2. Run "cd <path_to_BookManager>"
3. Run "source .initial_setup" [ sources env variables, which assists in configuring venv, mongodb and Flask]
4. Run "pytest --cov"
5. Run "flask run" 
---------------------------------------


Test coverage status :

TOTAL                                      219      7    97%
