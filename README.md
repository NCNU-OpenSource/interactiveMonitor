# interactiveMonitor
互動式監控系統

拍照軟體(fswebcam)
sudo apt-get install fswebcam

影像串流軟體(mjpg-streamer)
sudo apt-get install subversion libjpeg8-dev imagemagick libv4l-dev

svn co https://svn.code.sf.net/p/mjpg-streamer/code/

測試影片串流
cd code/mjpg-streamer</br>
sudo mjpg_streamer -i "./input_uvc.so -y -r 640x480" -o "./output_http.so -w ./www"</br>
打開http://IP:port[預設port 8080]
