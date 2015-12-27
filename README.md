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
```

####影像串流軟體(mjpg-streamer)
```
sudo apt-get install subversion libjpeg8-dev imagemagick libv4l-dev
svn co https://svn.code.sf.net/p/mjpg-streamer/code/
```

####測試影片串流
```
cd code/mjpg-streamer
sudo mjpg_streamer -i "./input_uvc.so -y -r 640x480" -o "./output_http.so -w ./www"
```
open browser @ http://IP:port [default port 8080]

####APP即時影片串流(android)
```
wget https://dl.google.com/dl/android/studio/ide-zips/1.5.1.0/android-studio-ide-141.2456560-linux.zip
tar -xzvf android-studio-ide-141.2456560-linux.zip
cd /android-studio/bin/
studio.sh
```
