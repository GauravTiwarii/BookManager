
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
Install following Python3 requirements :

1. Run "pip install virtualenv flask Flask-API mongoengine pytest pytest-cov requests"

----------------------------------------------
Run the App, using Following commands :

1. Run "virtualenv book_manager_env"
2. Run "source .initial_setup" [ sources env variables, which assists in configuring venv, mongodb and Flask]
3. Run "pytest --cov"
4. Run "flask run" 
---------------------------------------


Test coverage status :


\n---------- coverage: platform linux2, python 2.7.15-final-0 ----------

\nName                                     Stmts   Miss  Cover
\n------------------------------------------------------------
\napp/__init__.py                             51      0   100%
\napp/models.py                               10      0   100%
\napp/services/__init__.py                     0      0   100%
\napp/services/external_books.py              20      1    95%
\napp/utils/__init__.py                        0      0   100%
\napp/utils/book_processor.py                 49      3    94%
\napp/utils/db_utils.py                       16      3    81%
\ninstance/__init__.py                         0      0   100%
\ninstance/config.py                          18      0   100%
\ntests/__init__.py                            0      0   100%
\ntests/conftest.py                           14      0   100%
\ntests/test_APIs/__init__.py                  0      0   100%
\ntests/test_APIs/test_APIs.py                32      0   100%
\ntests/test_db_models/__init__.py             0      0   100%
\ntests/test_db_models/test_db_models.py       9      0   100%
\n------------------------------------------------------------
\nTOTAL                                      219      7    97%

