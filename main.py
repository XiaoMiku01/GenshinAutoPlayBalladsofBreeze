import win32gui
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import pyautogui as pg
from merge import manyimgs

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

app = QApplication(sys.argv)
imgB = cv2.imread('B.png')
hash1 = aHash(imgB)
while 1:
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot1.jpg")
    # print('ok')
    img1 = cv2.imread("screenshot1.jpg")
    w,a,s,d= img1[332:468, 338:474],img1[472:608,198:334],img1[612:748,338:474],img1[472:608,470:610]
    i,j,k,l=img1[332:468,1128:1264],img1[472:608,985:1125],img1[612:748,1128:1264],img1[472:608,1270:1406]
    imgs = manyimgs(1, ([w,a,s,d],[i,j,k,l]))
    # 展示多个
    cv2.imshow("mutil_pic", imgs)
    m=15
    if cmpHash(hash1,aHash(w))<m:
        pg.press("w")
        print('w')
    if cmpHash(hash1,aHash(s))<m:
        pg.press("s")
        print('s')
    if cmpHash(hash1,aHash(a))<m:
        pg.press("a")
        print('a')
    if cmpHash(hash1,aHash(d))<m:
        pg.press("d")
        print('d')
    if cmpHash(hash1,aHash(i))<m:
        pg.press("i")
        print('i')
    if cmpHash(hash1,aHash(j))<m:
        pg.press("j")
        print('j')
    if cmpHash(hash1,aHash(k))<m:
        pg.press("k")
        print('k')
    if cmpHash(hash1,aHash(l))<m:
        pg.press("l")
        print('l')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
