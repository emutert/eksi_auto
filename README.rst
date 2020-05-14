============
eksi-engelle
============

This is a short guide for the eksi-engelle application to run.

Project Structure
-----------------
- eksi-engelle blocks all users (authors and readers) from favorite list of targeted entry by using selenium webdriver,

- shows the total blocked user count,

- blocks spesific suser.

Virtualenv
~~~~~~~~~~

As an alternative to Anaconda, you can also use ``virtualenv``, to define your
Python 3 environment. You are required to have a Python 3 installed in your
workstation.

You can find the `virtualenv installation procedure`_ on the PyPA website.

Once you've installed Python 3 and ``virtualenv``, you will have to setup a
``virtualenv`` environment:

.. code-block:: sh

  # navigate to the eksi-auto directory
  cd eksi-auto

  # create the virtual environment for eksi-engelle
  virtualenv -p YOUR_LOCAL_PYTHON3_PATH eksi_venv

  # activate the virtual environment
  source eksi_venv/bin/activate

You can deactivate the virtual environment with the following command:

.. code-block:: sh

  deactivate

.. _`virtualenv installation procedure`: https://virtualenv.pypa.io/en/stable/installation/

Please remember that you may have to reactivate the virtual environment if you
open a new Terminal or Command Prompt window, or restart your system.

Dependencies and Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- FireFox 76.0.1 

- Selenium geckodriver 0.26.0 
`<https://github.com/mozilla/geckodriver/releases>`_.

- selenium>=3.141.0

- prompt_toolkit>=3.0.5

After activated your virtual environment you can install eksi-engelle :

.. code-block:: sh
  
  python setup.py install
  
You can copy geckodriver :

.. code-block:: sh

    $chmod +x copy_driver.sh
    $./copy_driver.sh



Running the Application
-----------------------

After eksi-engelle installation completed and geckodriver copied to correct folder you can run eksi-engelle. 

.. code-block:: sh
  
    $eksi-engelle 

You can use eksi-engelle cli after your authentication completed. 

.. code-block:: sh
        $eksi-engelle
        Eksi Suser Engelle
        Browser is initializing...
        You need to Login
        email    :your@mail.com
        password :
        

You can use tab key to complete the command after first character as shown in below. 

  S + tab for Suser
  
  E + tab for EntryNo
  
  B + tab for Blocked Count
  
You can leave eksi-engelle with keyboard interrupt by `ctrl + d`. eksi-engelle singout your session,
closes all the browser windows and terminates the WebDriver session. 

.. code-block:: sh

            $eksi-engelle
            Eksi Suser Engelle
            Browser is initializing...
            You need to Login
            email    : your@mail.com
            password : 
            Login successful
            >
            S + tab for Suser 
            E + tab for EntryNo 
            B + tab for Blocked Count 
            >EntryNo xxxx
            Fav list is blocking
            >EntryNo yyyy
            Fav list is blocking
            >Blocked Count
            >***** engellenmiş.
            >
            GoodBye!
            $

