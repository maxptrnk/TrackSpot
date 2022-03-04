# INFOB318-template




<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #8a6d3b;; background-color: #fcf8e3; border-color: #faebcc;">

- Acronyme: **TrackSpot**
- Titre: **Application de tracking et de recommandation pour Spotify**
- Client: **Valentin Delchevalerie**
- Étudiant: **Maxime Petrenko**
</div>


<!-- --------------------------------------------------
# **About TrackSpot** -->
--------------------------------------------------
# **Installation of TrackSpot**
## **Requirements**
* python 3.7 ([get it here](https://www.python.org/downloads/))
* pip


## **Setup environment**
1. Clone the repository
2. Open a terminal
3. In the same directory where the repo is, you must set up an isolated environment and download the required packages for the application so that it does not mess up with other existing versions of python and packages.


### Install virtual environment

```
pip install virtualenv
```

### Create the virtual environment

```
virtualenv venvTrackSpot
```
### Activate the virtual environment
Mac OS / Linux

```
source mypython/bin/activate
```

Windows
```
mypthon\Scripts\activate
```




## **Launch App**

Where your are this directory: 'TrackSpot/code', you can install requirements with the following command


```
pip install -r requirements.txt
```

And now you can run the app with following commands
> This may vary depending on your OS.


### Windows: Powershell

```ps
$env:FLASK_APP=./app.py 
flask run
```
### Windows: Command prompt
```cmd
set FLASK_APP=app.py
flask run
```

### Mac OS / Linux

```bash
export FLASK_APP=app.py
flask run
```

You should receive a link to localhost, click on and enjoy!!

--------------------------------------------------







