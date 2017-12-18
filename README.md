# Webapp for Reddit Emblem Team O,
### by [u/](https://www.reddit.com/user/Novikov_Principle)Novikov_Principle
This is the repo for the RE Team O Webapp, which tracks ally and enemy stats and positions on the map, and holds convoy and shop information.

The program attempts to follow the format of the [other Team Webapps](https://redditemblem.github.io/), with the main difference being that this webapp was written in **Python 2** with **Flask**, instead of JavaScript.

This application is currently deployed on [Heroku](https://team-o-webapp.herokuapp.com)!

As far as I know, the program should work on any Desktop browser. (Not tested on mobile platforms.)

## Webapp requirements
- Python 2.7.14
- Flask
- gunicorn
- gspread, and the Google Drive API
- a decent Internet connection

## Additional details
This program works using Python Flask, along with its built in Jinja2 Templating, along with HTML and CSS formatting. Admittedly, the code itself could see vast improvements, which will be listed in the "Future Features" section.

Due to it being written in Python, the webapp was deployed on Heroku instead of Github.io.

Part of the webapp (namely, /static/spreadsheet.py) relies on Anton Burnashev's [gspread](https://github.com/burnash/gspread) Python package. When run offline, spreadsheets.py creates a CSV file containing the general stats needed for the webapp to function, made possible with gspread. Although the resulting CSV still needs to be manually edited and split into two separate files (for Main maps and Gaiden maps), the script itself saves at least half an hour of separate data scraping, which adds up after each turn released.



## Helpful links
- [/r/](https://www.reddit.com/r/Reddit_Emblem/)Reddit Emblem
- Python Flask [documentation](http://flask.pocoo.org/docs/0.12/)
- [/r/flask](https://www.reddit.com/r/flask/)
- Jinja 2 Template [documentation](http://jinja.pocoo.org/docs/2.10/templates/)
- The [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world-legacy), by Miguel Grinberg
- Python [csv](https://docs.python.org/2/library/csv.html) documentation, used in [/static/spreadsheet.py](https://github.com/NovikovPrinciple/RE/blob/master/static/spreadsheet.py)
- [w3Schools](https://www.w3schools.com/), with helpful tutorials for HTML, CSS, JavaScript, and SQL
- [Bootstrap](http://getbootstrap.com/), helpful pre-made, open-source JS code and CSS templates
- The Python + gspread Twilio [tutorial](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html), by Greg Baugues
- [gspread], a Python package by Anton Burnashev
- The [Google Sheets API Reference](https://developers.google.com/sheets/api/reference/rest/)
- datademofun's Heroku deployment [tutorial](https://github.com/datademofun/heroku-basic-flask#tldr)/documentation for Flask apps

## Future Features (in no particular order)
* improved [Popover](http://getbootstrap.com/docs/4.0/components/popovers/) formatting, including item/weapon/skill descriptions and stat breakdowns (Base + etc.)
* enemy Movement and Attack ranges on-click
* proper CSS for the Webapp's [index](https://team-o-webapp.herokuapp.com/index) page
* an actual [Shop](http://team-o-webapp.herokuapp.com/shop) page, featuring Ally inventories, Gold, and Ore totals, and an item list with prices
* tooltip text that shows Terrain information when the mouse hovers over specific Map spaces ([whoa, technology!](http://i0.kym-cdn.com/entries/icons/original/000/022/065/image.png))