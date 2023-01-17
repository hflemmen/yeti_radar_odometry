xhost +local:root
#docker run -it --network host -v /home/henrik/Data/oxford:/oxford/ -v /home/henrik/Results/yeti:/res/   keenan-yeti-1.0 "cd res &&  python3 /catkin_ws/src/yeti_radar_odometry/scripts/evaluate_odometry.py"
docker run -it --network host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
 -v /home/henrik/Data/oxford:/oxford/ -v /home/henrik/Results/yeti:/res/ \
   keenan-yeti-1.0 "cd res &&  /catkin_ws/build/yeti/odometry --root /oxford/ --sequence 2019-01-10-14-36-48-radar-oxford-10k-partial --append test && cat accuracytest.csv"
#docker run -it --network host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" \
#--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
# -v /home/henrik/Data/oxford:/oxford/ -v /home/henrik/Results/yeti:/res/ \
#   keenan-yeti-1.0 "cd res &&  /catkin_ws/build/yeti/odometry --root /oxford/ --sequence polarlys --append _polarlys_test && cat accuracytest.csv"
