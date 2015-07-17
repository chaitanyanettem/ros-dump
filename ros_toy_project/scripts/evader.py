#!/usr/bin/env python
import roslib; roslib.load_manifest('lab1')
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3, Twist
import random

class move_robot:
	def __init__(self):
		self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
		rospy.init_node('move_robot')
		self.speed = 1.0; self.angle = 0.0

	def run(self):
		self.sub = rospy.Subscriber('base_scan', LaserScan, self.callback)
		rospy.spin()

	def callback(self, scan):
		range_ahead = min(scan.ranges)

		if range_ahead < 1.0:
			rospy.loginfo("Here")
			self.speed = 0.0; self.angle = random.randrange(-1,1)
		else:
			self.speed = 1.0; self.angle = 0.0

		self.pub.publish(Twist(Vector3(self.speed,0,0), Vector3(0,0,self.angle)))

if __name__ == '__main__':
	controller = move_robot()
	try:
		controller.run()
	except ROSInterruptException:
		pass
