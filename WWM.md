okay what are we making?
- a daemon, or a program that keeps running dormantly in the background handly necessary tasks
such as NTP Network Time Protocol, something about time difference between your device and other device on your network
or maybe
- another example would be bluetooth handler. In the case of Linux, bluetoothctl is that program which runs as a background service
basically all layer 1 and 2 protocols have a handler

> We are making a daemon in python, that periodically checks if i'm logged into the college's captive portal or not.
> If i'm logged in, goes to sleep for another x number of seconds
> Else it uses the selenium webdriver and (blah blah) to log in to the captive portal in the background.
> Important thing is to be dormant in the background, which means to consume less memory in the background.

--- What we have already tried ---

1. Tried to capture the encrypted password from captive portal's script. No use.
    Because to capture the encrypted password, we need to modify the response we receive 
    from the captive portal, and then basically inject a line to pop out the needed thing.
    But to catch that needed thing, we will need a browser like structure, be it alerting or 
    console.log'ing. Would have to use selenium to do that. Why wouldn't directly log in using
    selenium then bro?
2. Kaafi khrab implementation of logic. The loop overall doesn't feel finesse. Needs work and advices. Also the captive portal for different 
    browsers was different. So if I logged in Chrome, Firefox would still need to be logged in. (INTERNET WORKED REGARDLESS, how hard could it be!!?)

==========FINISHED TASK=========

1. RESEARCH - about daemon library ✓ #not much documentation to work with, AI is gonna be the saviour
2. RESEARCH - about selenium library ✓ 
 * now i need the user to install selenium for chrome :(
 * but there is webdriver chromium for android as well, which means i can later integrate it into an android daemon later
3. RESEARCH - about how to make a good daemon in python  ✓
4. IMPLEMENTATION - basic selenium part of the script and looping  ✓


==========CURRENT TASK===========

1. RESEARCH - about how to make a good daemon in python ✓
 * error logs should be made, whenever daemon crashes. Also prevent crashing, prefer restarting the daemon altogether
 * backtracing is very important in a daemon.
 * overall, the program should be in a never ending loop.
2. RESEARCH - how daemonization works, can this be done without python-daemon module?
3. IMPLEMENTATION - automatic connection with ITS700X based on signal strength or maybe internet speed?
4. IMPLEMENTATION - construct similar selenium script for firefox and edge.
