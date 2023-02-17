import glob
import subprocess
import shlex


def run_yeti(dataset: str):
    subprocess.run(shlex.split("xhost +local:root"))
    command = shlex.split(
        f"""docker run -it --rm --network host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --name="yeti_{dataset}" 
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" 
    --volume="/home/henrik/.Xauthority:/root/.Xauthority:rw,z" 
     -v="/home/henrik/Data/oxford:/oxford/" -v="/home/henrik/Results/yeti:/res/" 
     -v="/home/henrik/Repos/yeti_radar_odometry/:/catkin_ws/src/yeti_radar_odometry/" 
     keenan-yeti-1.0 "cd catkin_ws && catkin build && cd /res/ && /catkin_ws/build/yeti/odometry --root /oxford/polarlys/ --sequence {dataset} --append _{dataset}_polarlys && cat accuracytest.csv" """)
    print(command)
    subprocess.run(command)


def run_yeti_on_all():
    dataset_base = "/home/henrik/Data/oxford/polarlys/"
    dataset_paths = glob.glob(dataset_base + "*")
    datasets = [path.split("/")[-1] for path in dataset_paths]
    for dataset in datasets:
        print(dataset)
        run_yeti(dataset)


if __name__ == '__main__':
    # run_yeti('2018-06-17-13_42_00')
    run_yeti_on_all()