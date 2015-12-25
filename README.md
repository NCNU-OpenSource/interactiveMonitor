# interactiveMonitor
互動式監控系統

#實做材料
材料|成本
-----|-----
Raspberry Pi|免費(LSA提供)
攝影機|免費(茂林友情出借)

拍照軟體(fswebcam)<br>
sudo apt-get install fswebcam

影像串流軟體(mjpg-streamer)<br>
sudo apt-get install subversion libjpeg8-dev imagemagick libv4l-dev<br>
svn co https://svn.code.sf.net/p/mjpg-streamer/code/

測試影片串流
cd code/mjpg-streamer<br>
sudo mjpg_streamer -i "./input_uvc.so -y -r 640x480" -o "./output_http.so -w ./www"<br>
打開http://IP:port[預設port 8080]
