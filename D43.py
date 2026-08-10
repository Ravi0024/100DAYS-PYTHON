"""   virtual environment is a term used to describe a self-contained directory that contains a Python installation for a 
    particular version of Python, plus a number of additional packages. It allows you to manage dependencies for different projects 
    separately, avoiding conflicts between them.    
"""
"""
to create a virtual environment, you can use the venv module that comes with Python 3.3 and later.
example of creating a virtual environment using the venv module and activating it :

#create a virtual environment named "myenv" in the current directory
pyton -m venv myenv

#activate the virtual environment(linux/MacOs)
source myenv/bin/activate 

 # On Windows use 
 myenv\Scripts\activate.bat
"""
"""
Once the virtual environment is activated, any packages you install using pip will be installed in the virtual environment, rather than globally. 
To deactivate the virtual environment and return to the global Python environment,
you can use the deactivate command:
deactivate  
"""
#The "requirements.txt" file is a common convention in Python projects for specifying the dependencies required to run the project.
#It is a plain text file that lists the names and versions of the packages that the project depends on.
# This file can be used to recreate the same environment on another machine or to share the dependencies with other developers.
"to create a requirements.txt file, you can use the pip freeze command to generate a list of installed packages and their versions"
#pip freeze > requirements.txt
"TO install the dependencies listed in a requirements.txt file, you can use the pip install command with the -r option"
#pip install -r requirements.txt