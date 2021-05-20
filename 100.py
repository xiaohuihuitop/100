
import pyqtgraph as pg
import pandas as pd
import numpy as np
import re


from pyqtgraph.Qt import QtCore, QtGui



# import pyqtgraph.examples
# pyqtgraph.examples.run()

# while True:
#     pass

P = 0.2
I = 0
D = 0

point = 3633
inputv = 0
output = 0


amplitude = 100


out_max = 80
out_min = 1

CurrentError = 0
SumError = 0
LastError = 0
PrevError = 0

CurrentVal = 0
LastVal = 0

i_temp = 0



def  PID_Control():
    global P, I, D, point, inputv, output, amplitude, out_max, out_min, CurrentError, SumError, LastError, PrevError, CurrentVal, LastVal, i_temp, out_max, out_min
    maxo = 0
    mino = 0
    CurrentError = point-inputv

    i_temp = (I*CurrentError)+i_temp

    if i_temp > out_max:
            i_temp = out_max
    if i_temp < out_min:
        i_temp = out_min

    out = P*CurrentError + i_temp + D*(LastVal-CurrentVal)

    LastError = CurrentError
    LastVal = CurrentVal


    maxo = output + amplitude
    mino = output - amplitude
    if out > maxo:
        out = maxo
    if out < mino:
        out = mino


    if out > out_max:
        out = out_max
    if out < out_min:
        out = out_min

    output = out




pwDataarr = []
pwDataarr.clear()
pwpwm = []
pwpwm.clear()

for i in range(0,4096):
    inputv = i
    PID_Control()
    print(output)
    pwDataarr.append(output)
    pwpwm.append(i/4096*3.3*102.5)


win = pg.GraphicsWindow()

p1 = win.addPlot()

p1.plot(pwDataarr,pen = 'g')
p1.plot(pwpwm,pen = 'r')


def mouseMoved(evt):  # 鼠标显示坐标
    mousePoint = p1.vb.mapSceneToView(evt[0])
    p1.setTitle("小灰灰^_^---时间  X=%0.2f  高度  Y=%0.2f"  % (mousePoint.x(), mousePoint.y()))

proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)  #调用鼠标函数，实现鼠标数据显示

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

