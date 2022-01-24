# How to run the project

## *installing required stuff*

* Python
    * pip
* Django
* modules
___
### Python

To install python follow this link
[link is yet to come]()

For linux and mac users python comes installed. To check if it is type the following to a terminal

(for you ken everything shoud be fine)
```
python
```
if the above command shows something like..

```
Python 3.10.1 (main, Dec 18 2021, 23:53:45) [GCC 11.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

You are good to go. but if by anychance it starts with...
```
python 2.xx.xx (main ....)
```

this shows you are using python 2 and you need 3.5 and above try
```
python3
```
and if that doesnt fix it then ask me for help.


## pip

pip is a python package manager and it can be used to install packages. You need to install it but linux and mac comes with it.

### Set up project.

Once pip is installed everything else becomes simple.

Download the project as a folder ie ```comments```

once downloaded open your terminal and change location to that folder. eg if its on downloads.

```
cd ~/Downloads/comments
```

once in that folder print the content to confirm you have the files i.e
```
ls
```
which should output...
```
comments  db.sqlite3  landing  manage.py  requirements.txt  sdb.sqlite3  static  tutorial.md
```

That will show that it is complete. 

### install packages

once the project folder is ready use pip to install the necessary modules saved on requirements.txt
```
pip install -r requirements.txt
```
for one using ```python3``` command
```
pip3 install -r requirements.txt
```

That will install all the python packages you need.

next run the server ..
```
python manage.py runserver
```
for python3 command user
```
python3 manage.py runserver
```
this will output
```
[pc@my-pc comments]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 24, 2022 - 10:05:14
Django version 4.0.1, using settings 'comments.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

meaning server is up and running..

Use or click this link to see it [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

if any error shows its most likely an expired token. It is changed every few hours.