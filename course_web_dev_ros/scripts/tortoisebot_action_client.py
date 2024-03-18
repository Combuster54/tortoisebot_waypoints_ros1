#! /usr/bin/env python3
import rospy
import time
import actionlib

from course_web_dev_ros.msg import WaypointActionFeedback, WaypointActionResult, WaypointActionAction, WaypointActionGoal
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf import transformations
import math

class WaypointClientClass(object):

    # create messages that are used to publish feedback/result
    _feedback = WaypointActionFeedback()
    _result = WaypointActionResult()

    # topics
    _pub_cmd_vel = None
    _sub_odom = None

    # go to point vars
    # robot state variables
    _position = Point()
    _yaw = 0
    # machine state
    _state = 'idle'
    # goal
    goal_pos = Point()

    point_1 = Point()
    point_1.x = 0.6755 
    point_1.y = -0.4972

    point_2 = Point()
    point_2.x = 0.7037
    point_2.y = 0.4217

    point_3 = Point()
    point_3.x = 0.283
    point_3.y = 0.416

    point_4 = Point()
    point_4.x = 0.23250
    point_4.y = 0.0552

    point_5 = Point()
    point_5.x = -0.118690
    point_5.y = -0.006254

    point_6 = Point()
    point_6.x = -0.103782
    point_6.y = -0.009988

    #Left behind start line
    point_7 = Point()
    point_7.x = -0.64027
    point_7.y = -0.5518

    point_8 = Point() 
    point_8.x = -0.5237519914202051
    point_8.y = -0.490348969010396

    point_9 = Point()
    point_9.x = -0.2160
    point_9.y = 0.44149

    point_10 = Point()
    point_10.x = -0.5956
    point_10.y =  0.4430

    # parameters
    _yaw_precision = math.pi / 90 # +/- 2 degree allowed
    _dist_precision = 0.05

    def __init__(self):
        # creates the action server
        self.action_client = actionlib.SimpleActionClient('/tortoisebot_as', WaypointActionAction)
       
        rospy.loginfo("Action client ready")

    def start_client(self):

        rospy.loginfo("Action client has been started")

        self.client.wait_for_server()

        goal = WaypointActionGoal(self.point_1)
        self.client.send_goal(goal, feedback_cb=self._feedback_callback)

        self.state_result = self.action_client.get_state()

        # define a loop rate
        self._rate = rospy.Rate(25)


if __name__ == '__main__':
    rospy.init_node('tortoisebot_clt')
    WaypointClientClass()
    rospy.spin()