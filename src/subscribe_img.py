#!/usr/bin/env python
import rospy
import roslib 
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped, TransformStamped
from gazebo_msgs.srv import *
import math

# Because of transformations
import tf_conversions
import tf2_ros

def call_receive_custom_img(msg):
    rospy.loginfo('Message Received')
    if msg:
        test = msg.data
        print(ord(test[0]))


if __name__ == "__main__":
    rospy.init_node('img_listener', anonymous=True)
    sub = rospy.Subscriber('/custom_img',Image, call_receive_custom_img)
    rospy.spin()