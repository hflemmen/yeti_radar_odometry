#docker run -it --network host -v /home/henrik/Data/oxford:/oxford/ -v /home/henrik/Results/yeti:/res/   keenan-yeti-1.0 "cd res &&  python3 /catkin_ws/src/yeti_radar_odometry/scripts/evaluate_odometry.py"
docker run -it --network host -v /home/henrik/Data/oxford:/oxford/ -v /home/henrik/Results/yeti:/res/   keenan-yeti-1.0 "ls /oxford/polarlys/radar/ && cd res &&  /catkin_ws/build/yeti/odometry --root /oxford/ --sequence polarlys --append _polarlys_test && cat accuracytest.csv"
