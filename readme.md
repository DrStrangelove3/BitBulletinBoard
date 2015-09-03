# BitBulletinBoard v0.1 ALPHA

This project is a decentralized bulletin board program that is inspired by Reddit. The software uses PyBitmessage to send posts, votes and images between nodes in a way that is secure and private. The decentralized nature of the software also makes it difficult to shutdown or censor. BitBulletinBoard is meant to be run on your local machine or on a local server on your LAN. It is best to leave the software running 24/7 to support the network, but you can turn off the program for up to 4 days without missing any posts or votes.

This software is in alpha and is potentially buggy and not feature complete. I will be adding comments, one click setup script, and more in later releases.

## Dependencies

*   Python 2.7.* (Note: There are compatability issues with Python 3)
*   PyBitmessage 0.4.4

## Installing and Running

The first step is to install PyBitmessage which can be found [here](https://bitmessage.org). The next step is to enable the API using the instruction found [here](https://bitmessage.org/wiki/API_Reference) and you can find your key.dat file with the reference [here](https://bitmessage.org/wiki/Keys.dat). Make sure to use the username: "username", password: "password" and port 8442\. The scripts in the cgi-bin folder need to have 'execute permissions' for 'everyone' on Linux. Finally, make sure PyBitmessage is running and run the command "python -m CGIHTTPServer" in the root folder of this project. You can add the chan BitBulletinBoardTest BM-2cWdS9Tdh2WWvuH3ACvV62iVtLCQxbz2fG which has some sample posts to test that BitBulletinBoard is working. You can access BitBulletinBoard at [http://localhost:8000/](http://localhost:8000/).

## Screenshots

![Screenshot 1](https://raw.githubusercontent.com/DrStrangelove3/BitBulletinBoard/master/Screenshots/BitBulletinBoard-ScreenShot1.jpg)

![Screenshot 2](https://raw.githubusercontent.com/DrStrangelove3/BitBulletinBoard/master/Screenshots/BitBulletinBoard-ScreenShot2.jpg)

## Development

Feel free to contribute code, file bug reports or send feedback to the email address DrStrangelove@tutanota.com.  
You can contribute to this project by donating to this Bitcoin address: 1Fjq1HgSDKPPSCk34eBun6nap3ZAUxypzc  
And don't forget to support [Bitmessage](https://bitmessage.org/wiki/Main_Page) which made this project possible.
