<h1 align= "center"><b>Blogger</b></h1> 

<div align= "center"> 
Blogger is a basic blogging application which includes user to create account and post their views.
</div>


<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/harsh-kumar-1a287617a/)
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/harsh-9in/Blogger/issues)
[![License](https://img.shields.io/github/license/harsh-9in/Blogger?style=flat-square)](https://github.com/harsh-9in/Blogger/)
[![Forks](https://img.shields.io/github/forks/harsh-9in/Blogger.svg?logo=github)](https://github.com/harsh-9in/Blogger/network/members)
[![Stargazers](https://img.shields.io/github/stars/harsh-9in/Blogger.svg?logo=github)](https://github.com/harsh-9in/Blogger/stargazers)
[![Issues](https://img.shields.io/github/issues/harsh-9in/Blogger.svg?logo=github)](https://github.com/harsh-9in/Blogger/issues)
[![Contributors](https://img.shields.io/github/contributors/harsh-9in/Blogger.svg?logo=github)](https://img.shields.io/github/contributors/harsh-9in/Blogger)

<br>



## Tech Stack

- **Frontend:** HTML/CSS
- **Backend:** Django

## Quick Start :

- **Fork it** :

Get your own Fork/Copy of repository by clicking `Fork` button right upper corner.<br><br>

- **Clone**:

```sh
$ git clone https://github.com/harsh-9in/Blogger.git
$ cd Blogger/mysite
```

- **Branching**

```
$ git checkout -b [your_branch_name]
```

- **Make Changes in Source Code**

#### Setting up Project

- Create a Virtual Environment

```
python3 -m venv env
```

- Activate the Virtual Environment

  - On Windows
    ```
    env\Scripts\activate
    ```
  - On Linux or MAC
    ```
    source env/bin/activate
    ```

- Install dependencies using

```
pip install -r mysite/requirements.txt
```


- Setting up mandatory file
```
A .env.example file is present in the mysite folder you have to copy the content of .env.example and paste it into
.env file (a file to be made in the same folder as .env.example file) so that settings.py file take all the 
configurations from .env file.
```


- Make migrations using

```
python manage.py makemigrations
```

- Migrate Database

```
python manage.py migrate
```

- Create a superuser

```
python manage.py createsuperuser
```

- Run server using

```
python manage.py runserver
```

- **Stage your Changes and Commit**

```
# For adding/Staging Changes

$ git add .


# For Commiting Changes

$ git commit -m "<your commit message>"

```

- **Push your Commit to Repo**

```
$ git push origin <branch_name>
```

## Project Structure

/<br>
|- .github<br>
|- mysite : Project Directory<br>
|&ensp;&ensp;&ensp;&ensp;|- blog : Application for the blogs<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- migrations : Contains files that helps us to make the changes to the database schema as per the changes done in the models.<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- static : All the static assets for the blog application<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- templates : All the application specific templates<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- \_\_init**.py<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- admin.py : In this we register the models with the Django admin application<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- apps.py : In this we register/configure all the common files for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- forms.py : Contains all the forms for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- models.py : Contains all the models for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- tests.py : Contains all the tests for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- urls.py : Contains all the urls which are specific for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- views.py : Contains all the views for the app<br>
|&ensp;&ensp;&ensp;&ensp;|- media : The media files related to the blogs and users<br>
|&ensp;&ensp;&ensp;&ensp;|- mysite : Python project package<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- \_\_init**.py<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- asgi.py : Entry point for the ASGI servers<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- settings.py : All the configurations for your project<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- urls.py : All the URLs for the Django project<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- wsgi.py : Entry point for the WSGI servers<br>
|&ensp;&ensp;&ensp;&ensp;|- staticfiles : To keep the static assets like images, CSS, JavaScript<br>
|&ensp;&ensp;&ensp;&ensp;|- users : Application for users<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- migrations : Contains files that helps us to make the changes to the database schema as per the changes done in the models.<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- templates : All the application specific templates<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- \_\_init\_\_.py<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- admin.py : In this we register the models with the Django admin application<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- apps.py : In this we register/configure all the common files for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- backends.py : Contains the backend specific authentication functions<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- forms.py : Contains all the forms for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- models.py : Contains all the models for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- tests.py : Contains all the tests for the app<br>
|&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;|- views.py : Contains all the views for the app<br>
|&ensp;&ensp;&ensp;&ensp;|- db.sqlite3 : Database file created when you run the migrate command<br>
|&ensp;&ensp;&ensp;&ensp;|- manage.py : A command line utility<br>
|&ensp;&ensp;&ensp;&ensp;|- Procfile : A file required for the Heroku Web applications to define the applications process types and entry points<br>
|&ensp;&ensp;&ensp;&ensp;|- requirements.txt : Contains all the modules and libraries required for the project.<br>
|&ensp;&ensp;&ensp;&ensp;|- runtime.txt : specify the Python runtime<br>
|- .gitignore : Contains all the files and folders which needs to be ignored while pushing the code to the Git<br>
|- [CODE_OF_CONDUCT.md](https://github.com/harsh-9in/Blogger/blob/master/CODE_OF_CONDUCT.md) : Code of Conduct to be followed<br>
|- [CONTRIBUTORS.md](https://github.com/harsh-9in/Blogger/blob/master/CONTRIBUTORS.md) : See the contributors of the project<br>
|- [LICENSE.md](https://github.com/harsh-9in/Blogger/blob/master/LICENSE.md) : See the License<br>
|- [README.md](https://github.com/harsh-9in/Blogger/blob/master/README.md) : Read all the instructions releated to the project<br>

## Contribution Guidelines

- Take a look at the guidelines to contribute to the project
- [CONTRIBUTING GUIDELINES](https://github.com/harsh-9in/Blogger/blob/master/CONTRIBUTING.md)

## Geeks behind the initiative

### Project Admin

**Harsh Kumar** -[Know more](https://github.com/harsh-9in)

### Project Mentors

-**Kajol Kumari**-[Know More](https://github.com/Kajol-Kumari) -**Swarnima Shukla**-[Know More](https://github.com/Swarnimashukla) -**Sarath Kaul**-[Know More](https://github.com/SKAUL05)

## Open Source Programs

- ### Contributor's Hack 2020
  Contributor's Hack 2020 is a program that helps students grow with ""OPEN SOURCE"". This initiative by **HakinCodes** provides you the best platform to improve your skills and abilities by contributing to vast variety of OPEN SOURCE Projects and opportunity to interact with the mentors and the Organizing Team.

<p align="center"><img src="https://user-images.githubusercontent.com/54139847/87952512-882a5600-cac7-11ea-939d-8304a641d8a9.png" height='415' width='450'/></p>

- ### NJACK Winter of Code 2020
  **NWoC** (NJACK Winter of Code) is a program by **NJACK** (The Official Computer Science Club of IIT Patna) that helps students understand the paradigm of Open Source contribution and gives them real world software development experience.

<p align="center"><img src="https://njackwinterofcode.github.io/images/nwoc-logo.png" height='450' width='600'/></p>

- ### Devscript Winter of Code 2020
  **DWOC** is an open source initiative taken by Devscript to help students and learners be acquainted with the different aspects that entail open source contribution. It helps the mentees get a taste of problem solving in the real world.

<p align="center"><img src="https://github.com/IshetaBansal/Blogger/blob/master/DWOC-logo.png" height='515' width='515'/></p>
