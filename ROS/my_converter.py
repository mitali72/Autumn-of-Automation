#!usr/bin/env python

import rospy
from my_pkg.msg import Euler
from my_pkg.msg import Quat
import numpy as np

	
class Quat_to_euler():

    def __init__(self):
        
        self.euler_msg = Euler()
        
        
        sub  = rospy.Subscriber("topic1", Quat, self.callback)
        pub = rospy.Publisher("topic2", Eulers)


        while not rospy.is_shutdown():
         
              pub.publish(self.euler_msg)
              r.sleep()
              
    def converter(self, q):
        sinr_cosp = 2*(q.w * q.x + q.y*q.z);
		cosr_cosp = 1 - 2*(q.x*q.x + q.y*q.y);
		r = np.arctan2(sinr_cosp, cosr_cosp)
		
		sinp = 2*(q.w * q.y - q.z*q.x);
		
		if(np.abs(sinp) >=1) :
			p = np.sign(sinp)*np.pi/2
		else :
			np.arcsin(sinp)
			
		
		siny_cosp = 2*(q.w * q.z + q.x*q.y)
		cosy_cosp = 1 - 2*(q.y*q.y + q.z*q.z)
			
		y = np.arctan2(siny_cosp, cosy_cosp)
	
        self.fill_euler_msg(msg, r, p, y)
        
    def fill_euler_msg(self, msg, r, p, y):
        self.euler_msg.roll  = r
        self.euler_msg.pitch = p
        self.euler_msg.yaw   = y
        
    def callback(data):
    
    	converter(data)
    	rospy.loginfo(self.euler_msg)

# Main function.    
if __name__ == '__main__':

    rospy.init_node('my_converter')
    r = rospy.Rate(1)
    try:
        convert = Quat_to_euler()
    except rospy.ROSInterruptException: pass
	
