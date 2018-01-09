Game of Life
------------
A simple Gampe of Life implementation.
A Sanbox for playing with Qt GUI and ```matplotlib.animation```.

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
