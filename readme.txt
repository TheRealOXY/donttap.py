v1.1

donttap.py
python based donttap bot

##

1. Setup

Install Python 3.7.3 (32bit), you don't have to install the same version, this is just recommended version.
From: https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe
While installing process click 'Add Python to PATH'.

Then run setup.py

##

2. Run

Right-click on donttap.py and hit 'Run with Python (the rocket icon one)'.
That's it.

BTW! You can stop the code with 'X' key. (It's glitchy sometimes)

##

3. ISSUES

Look down there if you have some issues with your code:


3a. The 'ImportError: DLL load failed while importing win32api: The specified module could not be found.' error.

This is a bit tricky one so listen carefully..

Open CMD as ADMINISTRATOR.
Type %localappdata% to your find pole left down.
Then go to 'Programs > Python > [whatever python versor you're using] > Scripts' now, copy the location.
Go back to CMD and type 'cd [your location]'.
Your console will now look like this 'C:\Users\[your pc]\AppData\Local\Programs\Python\[python version]\Scripts>'
Now type:

pip install pywin32
pip install pypiwin32

And finally:

pywin32_postinstall.py -install

Restart your computer.
Everything should work fine now :D



With any other errors contact me on my IG: @oxy.js :3
