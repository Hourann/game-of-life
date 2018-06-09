# This is an empty project for python [![Build Status](https://travis-ci.org/Hourann/game-of-life.svg?branch=master)](https://travis-ci.org/Hourann/game-of-life) 

# 接口设计
我们需要一个类Cell储存细胞状态，一个类Table控制整个游戏的逻辑。
## Cell
- `get_state`Cell需要保存自己的状态（生/死）
- `next`根据邻居的状态决定下一时间的状态。

## Table
- `__init__`初始化棋盘大小，Step 长度，初始图案
- `get_num_of_neighbor`提供方法根据坐标返回该坐标周围存活的领居数
- `next`提供一个步进方法让棋盘内所有的Cell进入下一状态
- `get_state`返回棋盘状态
- `set_state`设置棋盘状态
- `set_interval_time`设置迭代时间
- （optional）`pause`暂停迭代
- （optional）`refresh`:在棋盘内填充随机图案
- （optional）`flip_cell_state`翻转该格点状态


## Install dependences
```
pip install -r ./requirements.txt
```

## Test
```
nosetests
```

## Build
```
pyinstaller -F src/run.py --clean
```

## Run
```
./dist/run
```