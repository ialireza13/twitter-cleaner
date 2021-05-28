# Twitter History Cleaner
Value your privacy, delete your digital fingerprint
Using this code you can delete your twitter data choosing a cutoff date to delete tweets before that date.

You will need your twitter archive data and twitter API credentials and access token. (locally on your computer, DO NOT upload it anywhere or give it to anyone!)

## Instructions:
### 1. Download your Twitter history data:
Browse to Twitter in your browser, go to "Settings and privacy" -> "Your account" -> "Download and archive of your data".
Enter password and you will get a download link for your data in 24 hours or less in your email. Download that zip file and extract the tweet.js file from it. Copy it inside the project's directory.

### 2. Get Twitter API token and access code:
You can find online tutorials on how to get an API access from twitter, you will need 4 credentials: Consumer key, consumer secret, access token and access token secret. fill them in the credentials.py file.

### 3. Enter the desired cutoff date:
Open the driver.py file in a text/code editor and change the cutoff date to your desired date. Tweets before this date will be deleted.

### 4. Run!
Run the driver.py file in a terminal and wait for it to do its work. The logs will be accessible in the log file generated.
