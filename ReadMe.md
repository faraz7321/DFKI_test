# DFKI test
## [Google Colab notebook][3]
  - Note: you will need to upload the image which needs to be proccessed
  - This example uses the open source library [AprilTag][1]
  - I decided to work on Colab as it is quite robust and the latest tools were readily available.  

## Another example is based on the AprilTag python bindings created by [DuckieTown][2].
  - ```git clone https://github.com/faraz7321/DFKI_test.git```
  - ```cd DFKI_test/catkin_ws/``` and ```catkin build```
  - ```source devel/setup.bash```
  - script can be found in ```DFKI_test/catkin_ws/src/my_project/scripts/duckietown_at.py```
  - to install duckietown library
   ``` $ pip install dt-apriltags ```
  - run the test file using  ``` python3 -u "../duckietown_at.py -i <image_path>" ```
  - or with ```rosrun my_project duckietown_at.py -i <image_path>```


## Using ROS
I also tested [apriltag_ros][4] which is ROS wrapper of the AprilTag 3 visual fiducial detector.
to use it, i simply cloned the packages into my catkin workspace src directory.

```git clone https://github.com/AprilRobotics/apriltag_ros.git```

```git clone https://github.com/AprilRobotics/apriltag.git```

Build it using ```catkin build``` and source it. I was able to use the library with
```$ roslaunch apriltag_ros single_image_server.launch```
```$ roslaunch apriltag_ros single_image_client.launch image_load_path:=<absolute_path> image_save_path:=<absolute_path>```
but before, I needed to configure ```tags.yaml``` with the standalone tags and tag bundles which we want to detect and ```settings.yaml``` with the wrapper and apriltag core parameters. *I am still working on it*

[1]: https://github.com/AprilRobotics/apriltag "AprilTag"
[2]: https://github.com/duckietown/lib-dt-apriltags "DuckieTown"
[3]: https://colab.research.google.com/drive/1XdHN6jGLSZi8vrl14dyxkW4VbbkuZWID?usp=sharing "Google Colab notebook"
[4]: https://github.com/AprilRobotics/apriltag_ros "apriltag_ros"
