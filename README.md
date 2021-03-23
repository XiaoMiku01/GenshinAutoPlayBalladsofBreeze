# GenshinAutoPlayBalladsofBreeze
原神风花节自动弹琴辅助（已适配1920*1080分辨率）

### 语言环境
python3

已上传编译后的exe文件，没有Python环境的同学，就用它吧!

### exe文件下载链接
[百度云](https://pan.baidu.com/s/1dD-u09-yGpQ7p08Cy33SDA)提取码:7qmq

[github](https://github.com/XiaoMiku01/GenshinAutoPlayBalladsofBreeze/releases/download/2.1/v2.rar)

这两个下载包里的使用说明忘了改了，记得是1920*1080分辨率哦！
### 第三方库
PyQt5	(读取屏幕)
```shell
python3 -m pip install PyQt5
```
pyautogui	(键盘输入)
```shell
python3 -m pip install pyautogui
```
cv2		(图像识别)
```shell
python3 -m pip install opencv-python
```

win32gui
```shell
python3 -m pip install win32gui
```

### 使用方法
1.游戏分辨率调到1920*1080窗口化！！注意必须是窗口化！没有该选项的同学在全屏状态下按左alt键+回车键开启窗口化!!

2.打开游戏内弹琴开始界面，ps.不要将程序最小化，否则检测不到游戏界面！！

3.龙脊雪山的山洞或者去环境较暗的地方，面壁思过去弹，因为比较暗，识别更加准确。

4.运行 main.py。（没有python环境或第三方库就运行exe文件，windows下请右击已管理员权限运行！！）
```shell
python3 main.py
```

5.点击开始游戏，自动识别。

### 效果展示
![image](https://github.com/XiaoMiku01/GenshinAutoPlayBalladsofBreeze/blob/main/%E5%88%86%E6%95%B0.png?raw=true)
