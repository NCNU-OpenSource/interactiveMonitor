# interactiveMonitor
互動式監控系統

####實做材料
材料|成本
-----|-----
Raspberry Pi|免費(LSA提供)
攝影機|免費(茂林友情出借)
紅外線感測器|----
光線感測器|----
喇叭|----

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
#####開機啟動mjpg-streamer
```
sudo startstreamer.sh
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

####Android Studio
```
wget https://dl.google.com/dl/android/studio/ide-zips/1.5.1.0/android-studio-ide-141.2456560-linux.zip
tar -xzvf android-studio-ide-141.2456560-linux.zip
cd /android-studio/bin/
studio.sh
```

####References
- https://www.raspberrypi.org/forums/viewtopic.php?t=44039&p=350985
- http://askubuntu.com/questions/814/how-to-run-scripts-on-start-up
- https://developer.chrome.com/multidevice/webview/gettingstarted
- http://www.w3schools.com/css/tryit.asp?filename=tryresponsive_image3
