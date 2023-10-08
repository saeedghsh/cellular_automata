Game of Life
------------
A simple implementation of [Gampe of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
A Sanbox for playing with Qt GUI and `matplotlib.animation`.

```shell
$ git clone https://github.com/saeedghsh/GameOfLife.git
$ cd GameOfLife
$ pip install -r requirements.txt # numpy, matplotlib, PySide
$ python runMe.py # to run with GUI
$ pyth lib/GameOfLifeLib.py # to run simple animation (stop/start with mouse click)
```

![GUI snapshot](https://github.com/saeedghsh/GameOfLife/blob/master/gui/GUI.png)

Laundry List
------------
- [ ] add `requirement.txt`
- [ ] include steps of setting up and using Qt GUI

- [ ] include other rules
- [ ] implement other grid types
- [ ] include template-based initiation (e.g. glider)

- [ ] smoothlife? (continuious grid instead of discretized)
- [ ] smoothlife? (continuious life value instead of binary)

- [x] fix the animation bug
- [x] fix the horrible conway implementation

License
-------
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/GameOfLife/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
