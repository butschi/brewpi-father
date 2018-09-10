# brewpi-father
A tiny script to track temperatures from BrewPI to Brewfather.

This is just a 20 minute hack to get logging working.

## Prerequisites

- BrewPi setup with a RaspberryPI
- Brewfather account

## How to use this script

Upload the script to the RaspberryPi. I just put it into the /home/pi
directory.

Go to the Brewfather app and activate the BrewPiless utility under settings. Grab the
URL and paste it into the `post_update.py` script.

Also make sure the URL for your BrewPi is correct.

Create a virtual environment called venv and install requirements.

```
sudo apt-get install python3-venv

cd /home/pi/brewpi-father
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Add the script to crontab to run every 15 minutes.

```
crontab -e
```

Choose your favorite editor and add the line

```
*/15 * * * * /home/pi/brewpi-father/venv/bin/python3 /home/pi/brewpi-father/post_update.py
```

That's it. It started logging the temperatures to my Brewfather app. If you
have a Tilt or iSpindel or something, you need to adjust the script slightly.
