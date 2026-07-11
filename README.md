# web_dev_django
The repository contains guide and code to develop application using Django. It contains code for all the features present in Django. MVT model code applications are present too in this repository.

====================================================================================

I have added this in README.md file, as these are repetitive tasks which are performed when
we create any Django project from scratch.


1. Create a Django project.
   command: django-admin startproject employeeProject

2. Create an application inside the project.
   command: py manage.py startapp employeeapp

3. Register the application.
   Inside settings.py file register the application name: 'employeeapp' under Installed_Apps list

4. Create a templates folder on project level, as we would require html file for the frontend.
    command: mkdir templates

5. Create a static folder, this folder will hold two sub folders images and css.
   All the required stylesheets and images used will be stored here.

6. Now we need to tell Django that we have a templates directory in this particular location. So for that we need to add it in settings.py file.
   The TEMPLATE_DIR contains the directory location.
   Then register this variable to TEMPLATES variable holding list and inside that into the value of DIRS.

7. Now we need to follow the same steps for registering the static folder path.
   The static folder path is under STATIC_DIR variable.
   Add this variable inside the list the variable name should strictly be STATICFILES_DIRS = [STATIC]. 
   This variable name is internally used by pythons django module so if we use any other name it will not load the page correctly.


The above 7 steps is same for creating any Django project.
Whenever we create a Django project from scratch, we have to follow these 7 steps, so it works as a base for any Django project we create.
