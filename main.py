import tasks.lab2.block1 as t1
import tasks.lab2.block2 as t2
import tasks.lab2.block3 as t3
import numpy as np

arr = t1.createArr(10, 10)
print(arr)
print('Минимальный элемент: ' + str(t1.minEl(arr)))
print('Максимальный элемент: ' + str(t1.maxEl(arr)))
print(np.ravel(t1.sortMatrixInArr(arr)).T)
print(t1.diffElMenCol(t1.sortMatrixInArr(arr).T))
t2.buildPlot(-2, 2)
xInp=np.ravel(t1.sortMatrixInArr(arr).T)*10
t2.buildDoubleAxesOnFigure(x=xInp, x2=t1.sortMatrixInArr(arr))
t3.readFiles(r'src\geopandas')