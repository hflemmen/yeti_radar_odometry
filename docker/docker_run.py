import glob
import subprocess
import shlex
from enum import Enum

to_code_copy = {
    '2018-06-23-22_22_30': 'a',
    '2018-06-25-08_17_00': 'b',
    '2018-06-17-13_42_00': 'c',
    '2018-06-20-20_05_30': 'd',
    '2018-06-24-01_05_00': 'e',
    '2018-07-13-13_00_00': 'f',
    '2018-06-22-22_18_00': 'g',
    '2018-06-15-17_41_30': 'h',
    '2018-06-23-08_28_30': 'i',
}
def run_yeti(dataset: str, append="test"):
    subprocess.run(shlex.split("xhost +local:root"))
    command = shlex.split(
        f"""docker run -it --rm --network host --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --name="yeti_{dataset}" 
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" 
    --volume="/home/henrik/.Xauthority:/root/.Xauthority:rw,z" 
     -v="/home/henrik/Data/oxford:/oxford/" -v="/home/henrik/Results/yeti:/res/" 
     -v="/home/henrik/Repos/yeti_radar_odometry/:/catkin_ws/src/yeti_radar_odometry/" 
     keenan-yeti-1.0 "cd catkin_ws && catkin build && cd /res/ && /catkin_ws/build/yeti/odometry --root /oxford/polarlys/ --sequence {dataset} --append _{dataset}_polarlys-{append}" """)
    print(command)
    subprocess.run(command)


def run_yeti_on_all():
    dataset_base = "/home/henrik/Data/oxford/polarlys/"
    dataset_paths = glob.glob(dataset_base + "*")
    datasets = [path.split("/")[-1] for path in dataset_paths]
    for dataset in datasets:
        print(dataset)
        run_yeti(dataset)

param_Strings = {"zq": "float zq",
                 "sigma_gauss": "int sigma_gauss",
                 "patch_size":"int patch_size",
                 "cart_resolution": "float cart_resolution",
                 "ransac_threshold": "double ransac_threshold",
                 "nndr": "float nndr",
                 "inlier_ratio": "double inlier_ratio",}

def change_parameter(search_str: str, new_value):
    odometry_file = "/home/henrik/Repos/yeti_radar_odometry/src/odometry.cpp"
    with open(odometry_file, 'r') as f:
        lines = f.readlines()
    newline = None
    for i in range(len(lines)):
        if search_str in lines[i]:
            newline = f"\t{search_str} = {new_value};\n"
            lines[i] = newline
            break
    if newline is None:
        print("String not found")
        raise ValueError("String not found")
    else:
        with open(odometry_file, 'w') as f:
            f.writelines(lines)

def for_parameter_range(range: list, param):

    cfgs = []
    for value in range:

        change_parameter(param_Strings[param], value)
        run_yeti("2018-06-23-22_22_30", f"{param}_{value}")

def run_parameter_range():
    param = "inlier_ratio"
    param_range = [0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    # param_range = list(range(19, 30))
    for_parameter_range(param_range, param)


if __name__ == '__main__':
    # run_yeti('2018-06-20-20_05_30')
    # run_yeti('2018-06-24-01_05_00')
    # run_yeti('2018-06-17-13_42_00')
    # run_yeti_on_all()
    # change_parameter("float zq", 18)
    run_parameter_range()