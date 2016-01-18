# Druid Gameworks - Game asset manager
This web application is an asset manager. Create and keep track of tasks. Maintain a library of all the assets in the game and link them to Perforce changelists for ease of management.

# Instructions
Run pip install -r requirements.txt

Create a file called PerforceConnector.config and place it in the [root]/app directory

Paste the following in the file and update the values according to the perforce client to use (might need to create one for the web server where the dashboard will be hosted. Not sure yet)

[perforce]
port = ssl:[ip]:[port]
user = [username]
password = [password]
client = [client/workspace]