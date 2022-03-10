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


## **Set up API server**

**Set Up Your Account**

To use the Web API, start by creating a Spotify user account (Premium or Free). To do that, simply sign up at www.spotify.com.

When you have a user account, go to the Dashboard page at the Spotify Developer website and, if necessary, log in. Accept the latest [Developer Terms of Service](https://developer.spotify.com/terms/) to complete your account set up.

**Register Your Application**

Any application can request data from Spotify Web API endpoints and many endpoints are open and will return data without requiring registration. However, if your application seeks access to a user’s personal data (profile, playlists, etc.) it must be registered. Registered applications also get other benefits, like higher rate limits at some endpoints.

You can [register your application](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/), even before you have created it.

([Source](https://developer.spotify.com/documentation/web-api/quick-start/))




## **Setup environment**
1. Clone the repository
2. Open a terminal
3. In the same directory where the repo is, you must set up an isolated environment and download the required packages for the application so that it does not mess up with other existing versions of python and packages.


## **Requirements for environment**
* python 3.7 ([get it here](https://www.python.org/downloads/))
* pip

### Install virtual environment

```
pip install virtualenv
```


### Create the virtual environment and Activate the virtual environment
Mac OS / Linux
```
virtualenv venvTrackSpot
source mypython/bin/activate
```

Windows
```
python -m venv venvTrackSpot
venvTrackSpot\Scripts\activate
```




## **Launch TrackSpot**

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
You should receive a link to localhost. One last thing before you can use the application. You have to put the keys that will link TrackSpot to the API. 

## **Link TrackSpot and API**


To do so, take *Client_ID* and *Client_Secret* that you will found on the **dashboard** of your API server. Insert them in the respective locations in *authorization.py* file.

```
 self.CLIENT_ID = "YOUR CLIENT ID"
 self.CLIENT_SECRET = "YOUR CLIENT SECRET"
```
and then add in the **dashboard** => Edit Settings => Redirect URIs : http://127.0.0.1:5000/redirect/


Once it's all done, verify that flask server still up if it's so, you can now use [TrackSpot](http://127.0.0.1:5000). Enjoy!

--------------------------------------------------







