Instructions
```
cd ~/simulation_ws/src
git clone https://github.com/Combuster54/tortoisebot_waypoints_ros1 tortoisebot_waypoints
```
## Build simulation_ws
```
source ~/simulation_ws/devel/setup.bash
cd ~/simulation_ws
catkin_make && source devel/setup.bash
```

#Passed test
```
rostest tortoisebot_waypoints waypoints_test.test
```
#Failed test
 - Go to test folder and inside waypoint_test.py uncomment and comment these lines
   ![image](https://github.com/Combuster54/tortoisebot_waypoints_ros1/assets/98191055/5ccd27b3-862d-428f-9a21-981d801b42ba)
   
 - to:
 - 
   ![image](https://github.com/Combuster54/tortoisebot_waypoints_ros1/assets/98191055/73d547a6-71fa-48dd-a2ed-82dd14488041)
   
 - Then run the test again
```
rostest tortoisebot_waypoints waypoints_test.test
```
