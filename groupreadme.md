hey guys, 

I went ahead and rebuilt the server with a more basic approach. 

The `bx` folder in the django site, the `bxapp` folder is the bookxchange app thet we make.

yeah, it's a bit wierd, but thats how it works. It does make sense though. I set it up so that the root of the `bx` django app points to the `bxapp`

to run the server, you'll need to install the latest django with pip

`sudo pip update django`, then `python manage.py runserver`


