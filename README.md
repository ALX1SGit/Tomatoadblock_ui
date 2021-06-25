# Tomatoadblock_ui
This is a Python script that is using Flask to provide a Web service for monitoring Ad Blocker peformance (when Debug mode is enable inside Ads Blokcer for Tomato).

This is the first working version of the service, it need to be executed using Python3 and will use the port 3000 for the web service

Have in mind that the size of the logs needs to be configured on the router (Administration -> Logging -> Max Size before rotate). I configured value as 200KB (this script work with a single value)

![image](https://user-images.githubusercontent.com/86429971/123480701-1d3ba600-d5d9-11eb-8cf5-4b10ee8a67b0.png)

The program basically pull information from the logs and filter using tag for dns service. After that gather devices information from leases (to get the client name). And then made some calcs to prepare information to show into the ui.

The search bar and the PieHole graph has been done using js, in order to dont have to contact over again router for multiple searchs and grapsh.
