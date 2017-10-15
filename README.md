### Fantasy Premier League Scout :soccer: :trophy:

For people who can't pick football players good and want to learn to do other football manager stuff good too

Install with `pip install fplscout` (Just kidding it's not on pip yet)  
You can download from source and run `python setup.py install`

Usage:

~~~
fpl scout
fpl --help
fpl -rf ppg # use the points per game ranking function
fpl -bf lp_max # use the lp_max building function
~~~

Done. Enjoy your free fantasy football points.

This is extensible with custom ranking and team-building algorithms.

#### To-Do List

* Need to make sure it picks a good captain for your team, since they're worth twice as much.
* Need to make it care less about the value of players on the bench
* Need to do all the PyPi stuff to make this easily available
* Need to implement week-to-week factors such as home/away, strength of opposing team, and have a mode which scouts good transfers rather than for building a team