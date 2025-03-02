# REPO FOR RUNNING METAVISION DRIVER

## Steps to Launch

#### Terminal 1:

```bash
metavision_driver_ws$ ros2 launch metavision_driver driver_node.launch.py
```

#### Terminal 2:

```bash
metavision_driver_ws$ ros2 launch event_camera_renderer renderer.launch.py
```

#### Terminal 3:

To visualize the data from event camera
```bash
metavision_driver_ws$ ros2 run rqt_image_view rqt_image_view
```

#### Terminal 4:
To subscribe to the data from event camera 
```bash
metavision_driver_ws$ ros2 run event_cam_subscriber event_cam_subscriber 
```
