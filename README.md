# Tomatoadblock_ui
This is a Python script that is using Flask to provide a Web service for monitoring Ad Blocker peformance (like PiHole) (In order to work Debug mode must be enabled inside Ads Blokcer for Tomato {Advanced Settings -> Adblock)). I am using Vainilla Ads Bloquer but can be user for any custom scritps that uses dnsmasq to filter DNS resolutions for Ads Sources.

This is the first working version of the service, it need to be executed using Python3 and will use the port 3000 for the web service

I am working with a Linksys ea6500 v2 and Tomato v1.28.0000 -3.5-140 K26ARM USB AIO-64K

Have in mind that the size of the logs needs to be configured on the router (Administration -> Logging -> Max Size before rotate). I configured value as 200KB (this script work with a single file of logs). I was not sure for making this value way bigger, or creating a local copy inside the usb plagged into the router.

![image](https://user-images.githubusercontent.com/86429971/123483450-16169700-d5dd-11eb-907e-3f8965464399.png)

The program basically pull information from the logs and filter using tag for dns service. After that gather devices information from leases (to get the client name). And then made some calcs to prepare information to show into the ui.

The search bar and the PieHole graph has been done using js, in order to dont have to contact over again router for multiple searchs and graph.

Saw that subprocess is returning "more: can't open '|': No such file or directory ;more: can't open 'grep': No such file or directory; more: can't open 'dnsmasq': No such file or directory" but, this is not affecting the functionality of the program.

AFter start using it, i saw the CPU value went from 2% to 6%

If you want to test it, just execute the .py file with python, and if you want to meke it work add it to the boot after a sleep 30 (Administration -> Scripts -> Init) 

This is my very first personal sort of web page and Git.

I hope you ejonoy being able to wach how the Ads Blocker is working in your router.

ALX

