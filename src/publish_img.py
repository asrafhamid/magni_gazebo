#!/usr/bin/env python
import rospy
import roslib 
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
from geometry_msgs.msg import PoseStamped, TransformStamped
from gazebo_msgs.srv import *
import math

# Because of transformations
import tf_conversions
import tf2_ros

class ImgPublisher:
    def __init__(self):
        self.counter = 0
        self.image = None
        self.sub = rospy.Subscriber('/camera/rgb/image_rect_color',Image, self.call_receive_rgb_img)
        self.pub = rospy.Publisher('/custom_img', Image, queue_size=1)
        self.reset_service = rospy.Service('/reset_counter', SetBool, self.call_reset_counter)

    def call_receive_rgb_img(self, msg):
        self.counter = self.counter + 1
        print(self.counter)
        # self.image = msg.data
        self.pub.publish(msg)
    
    def call_reset_counter(self, req):
        if req.data:
            self.counter = 0
            return True, 'Counter reset'
        return False, 'Counter not reset'

if __name__ == "__main__":
    rospy.init_node('img_publisher', anonymous=True)
    ImgPublisher()
    rospy.spin()