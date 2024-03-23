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

![image](https://github.com/Combuster54/tortoisebot_waypoints_ros1/assets/98191055/06f909ce-7d67-403d-94f0-aedcf5e18607)
   
 - to:
![image](https://github.com/Combuster54/tortoisebot_waypoints_ros1/assets/98191055/e91d3abe-cfc7-425a-a38c-0d679bf232e0)

   
 - Then run the test again
```
rostest tortoisebot_waypoints waypoints_test.test
```
