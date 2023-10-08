
import rclpy
from rclpy.node import Node
from autoware_auto_control_msgs.msg import AckermannControlCommand, AckermannLateralCommand, HighLevelControlCommand, LongitudinalCommand
from autoware_auto_vehicle_msgs.msg import GearCommand, GearReport, SteeringReport, VelocityReport
from std_msgs.msg import Header
from builtin_interfaces.msg import Time

class NewPublisher(Node):

    def __init__(self):
        super().__init__('control_interface_test')
        
        # Publishers for the messages
        self.ackermann_control_command_publisher = self.create_publisher(AckermannControlCommand, 'ackermann_control_command_topic', 10)
        self.gear_command_publisher = self.create_publisher(GearCommand, 'gear_command_topic', 10)

        
        timer_period = 0.1  # 10Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        timestamp = Time(sec=int(self.get_clock().now().seconds_nanoseconds()[0]))

        # Create and publish each message
        ackermann_control_cmd = AckermannControlCommand()
        ackermann_control_cmd.stamp = timestamp
        self.ackermann_control_command_publisher.publish(ackermann_control_cmd)
         
        gear_cmd = GearCommand()
        gear_cmd.stamp = timestamp
        self.gear_command_publisher.publish(gear_cmd)

        self.get_logger().info('Messages Published')

def main(args=None):
    rclpy.init(args=args)
    new_publisher = NewPublisher()
    rclpy.spin(new_publisher)
    new_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()