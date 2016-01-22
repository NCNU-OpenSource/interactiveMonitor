### InteractiveMonitor
互動式監控系統

####發想緣起
```
雖然市面上已經有許多的監視器，但我們想以成本最低的方式製作出屬於自己的監視器，同時加上自己想要的功能。
一般監視器會需要佔用許多軟體空間儲存所錄下來的監視畫面，而我們的方法是只要偵測到有任何的動靜才會拍下當下的畫面，
同時傳送即時通知以及畫面到手機的APP，即能減少消耗我們PI 16GB寶貴的空間，也讓使用者不需24小時關注監視器也能即時知道當下鏡頭另一邊的情況。
```
####使用語法
```
Python, Shell Script, XML, Java
```
####困境與解決
```
紅外線感測器出狀況(接受訊息不穩定) : 改用超聲波感測器加程式碼
無獨立Public IP無法從外界查看監視器(但能從APP收到人體偵測推送提示)：在校內示範
Android推送需加入GCM服務，時間與能力上的不足：PushBullet提供免費簡單推送API
影像串流無法與拍照同時使用Webcam：使用mjpg-streamer內建抓圖功能
無法控制單一USB孔電源開關模擬LED燈開關：使用面包板GPIO接上小LED來模擬
```

####實做材料
材料|成本
-----|-----
Raspberry Pi|免費(LSA提供)
攝影機|免費(茂林友情出借)
紅外線感測器|NT$120（已淘汰）
光線感測器|NT$100
超音波感測器|NT$70
面包板|巴西友情贊助
LED燈|巴西友情贊助
線材|孟儒友情贊助

####模組整合
![整合](https://github.com/NCNU-OpenSource/interactiveMonitor/blob/master/images/IMG1.jpg)

####分工
```
展維：模組採購、電路連接、模組測試
昱恆：APP撰寫、即時訊息推送、整合模組功能、軟體測試
```
####拍照軟體(fswebcam)
```
sudo apt-get install fswebcam
fswebcam -r 1024*720 test.jpg
```

####影像串流軟體(mjpg-streamer)
```
sudo apt-get install subversion libjpeg8-dev imagemagick libv4l-dev
svn co https://svn.code.sf.net/p/mjpg-streamer/code/
cd code/mjpg-streamer
sudo mjpg_streamer -i "./input_uvc.so -y -r 640x480" -o "./output_http.so -w ./www"
```
open browser @ http://IP:port [default port 8080]
######開機啟動mjpg-streamer
```
sudo nano startstreamer.sh
```
Insert
```
#!/bin/sh

STREAMER=/home/pi/code/mjpg-streamer/mjpg_streamer
DEVICE=/dev/video0
RESOLUTION=640x480
FRAMERATE=30
HTTP_PORT=8080

$STREAMER -i "/home/pi/code/mjpg-streamer/input_uvc.so $DEVICE -y -r $RESOLUTION -f $FRAMERATE" -o "/home/pi/code/mjpg-streamer/output_http.so -w /home/pi/code/mjpg-streamer/www -p $HTTP_PORT"
```
Save and exit
```
crontab -e
```
Insert
```
@reboot /home/pi/startstreamer.sh
```
Save and exit
```
sudo chmod +x startstreamer.sh
./startstreamer.sh
```

####Android Studio
```
wget https://dl.google.com/dl/android/studio/ide-zips/1.5.1.0/android-studio-ide-141.2456560-linux.zip
tar -xzvf android-studio-ide-141.2456560-linux.zip
cd /android-studio/bin/
studio.sh
```

####References
- https://www.raspberrypi.org/forums/viewtopic.php?t=44039&p=350985
- http://askubuntu.com/questions/38661/how-do-i-run-sh-files-in-terminal
- http://askubuntu.com/questions/814/how-to-run-scripts-on-start-up
- https://developer.chrome.com/multidevice/webview/gettingstarted
- http://www.w3schools.com/css/tryit.asp?filename=tryresponsive_image3
- https://www.youtube.com/watch?v=2QL5k235258
- http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/
- http://www.thirdeyevis.com/pi-page-2.php
- http://stackoverflow.com/questions/22575532/how-to-take-picture-with-mjpg-streamer
- http://stackoverflow.com/questions/2467609/using-wget-via-python
- http://stackoverflow.com/questions/9860680/python-overwrite-previous-line
- http://stackoverflow.com/questions/3916330/android-webview-webpage-should-fit-the-device-screen
