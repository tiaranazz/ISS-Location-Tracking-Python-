#This is a Python to track the real time location of ISS Space Ship. This project is using 'conda' base. To start, you need to do the following;

1. Download Visual Studio Code
2. Download Anaconda on www.anaconda.com
3. Open powershell/command prompt
    4. #Install plotting package to create the map, plotting the location of the ISS by entering the code; conda install --c ploty plotly
    5. Proceed the installation by pressing keyword 'y'
    6. Download any of the imports (if you're having trouble in executing the code) by entering the code; conda install geocoder, conda install requests, conda          install tweepy/conda install -c conda-forge tweepy
7. Open Visual Studio Code and install Python in the Extensions section by searching for Python. Follow as prompted.


#This project comprises of three different working files.

ISSTracking_Tiara file will display results in the iss.txt file where it shows the number of astronauts onboard and the current latitude & latitude. 
The second windows prompt is the Python Turtle Graphics, showing the world map and the real time location of the ISS Space Station that refreshes every 5 seconds.
The history of the location is displayed in the Terminal section in the Visual Studio Code IDE.
p/s: I'm still working on how to get the user time input (Task: Getting the location of the ISS at a specific time)

ISSTracking_Tiara_Weather file will display weather forecast for any given Country/City entered by the user.
You may input the location in the Terminal section in the Visual Studio Code IDE.
The results are also displayed in the Terminal section.

p/s: The third file is still in progress (I will update the working file into this repository). The intended system if to get Tweets about any input hashtag from user. I need to wait for twitter response in getting the API key.
