import win32gui
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import pyautogui as pg
from merge import manyimgs
import  numpy as np
import time
hwnd_title = dict()

# 均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8))
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n

def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t == "原神":
        hwnd=h
        break
imgB = cv2.imread('./image/B.png')
hash1 = aHash(imgB)
app = QApplication(sys.argv)
print("请点击开始游戏。")
while 1:
    screen = QApplication.primaryScreen()
    abc = screen.grabWindow(hwnd).toImage()
    s = abc.bits().asstring(abc.width() * abc.height() * abc.depth() // 8)
    img1 = np.frombuffer(s, dtype=np.uint8).reshape((abc.height(), abc.width(), abc.depth() // 8))
    w,a,s,d= img1[395:395+180,395:395+180],img1[557:557+180,227:227+180],img1[722:722+180,393:393+180],img1[557:557+180,563:563+180]
    i,j,k,l=img1[395:395+180,1343:1343+180],img1[557:557+180,1180:1180+180],img1[722:722+180,1343:1343+180],img1[557:557+180,1513:1513+180]
    try:
        imgs = manyimgs(1, ([w,a],[s,d],[i,j],[k,l]))
    except:
        print('程序出错！请确保原神在前台，不要最小化!')
        break
    m = 14
    if cmpHash(hash1, aHash(w)) < m:
        pg.press("w")
        print('w', cmpHash(hash1, aHash(w)))
    if cmpHash(hash1, aHash(s)) < m:
        pg.press("s")
        print('s', cmpHash(hash1, aHash(s)))
    if cmpHash(hash1, aHash(a)) < m:
        pg.press("a")
        print('a', cmpHash(hash1, aHash(a)))
    if cmpHash(hash1, aHash(d)) < m:
        pg.press("d")
        print('d', cmpHash(hash1, aHash(d)))
    if cmpHash(hash1, aHash(i)) < m:
        pg.press("i")
        print('i', cmpHash(hash1, aHash(i)))
    if cmpHash(hash1, aHash(j)) < m:
        pg.press("j")
        print('j', cmpHash(hash1, aHash(j)))
    if cmpHash(hash1, aHash(k)) < m:
        pg.press("k")
        print('k', cmpHash(hash1, aHash(k)))
    if cmpHash(hash1, aHash(l)) < m:
        pg.press("l")
        print('l', cmpHash(hash1, aHash(l)))
    time.sleep(0.05)
cv2.destroyAllWindows()
input('请重启程序')
