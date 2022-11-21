Google Colab: https://colab.research.google.com/drive/1MEP59MF5hHvQMyfxJXglxgVy5iLYFS-7?usp=sharing
Note: you will need to upload the image which needs to be proccessed
This example uses the open source library "AprilTag"
github: https://github.com/AprilRobotics/apriltag

Another example is based on the AprilTag python bindings created by duckietown.
github: https://github.com/duckietown/lib-dt-apriltags
you can install it with pip
$ pip install dt-apriltags

I also tested apriltag_ros which is ROS wrapper of the AprilTag 3 visual fiducial detector.
to use it, i simply created my catkin workspace, cloned package into my src directory
and built it. I was able to use it with
$ roslaunch apriltag_ros single_image_server.launch
$ roslaunch apriltag_ros single_image_client.launch image_load_path:=<absolute_path>
image_save_path:=<absolute_path>
but before, I needed to configure tags.yaml with the standalone tags and tag bundles which we want to detect and settings.yaml with the wrapper and apriltag core parameters. _I am still working on it_