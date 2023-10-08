
import rclpy
from rclpy.node import Node
from autonoma_msgs.msg import PowertrainData, RaceControl, ToRaptor, VehicleData, VehicleInputs

class DallaraInterfaceTestSubscriber(Node):

    def __init__(self):
        super().__init__('msg_subscriber')
        
        # Subscribers for the messages
        self.create_subscription(PowertrainData, '/powertrain_data', self.powertrain_data_callback, 10)
        self.create_subscription(RaceControl, '/race_control', self.race_control_callback, 10)
        self.create_subscription(ToRaptor, '/to_raptor', self.to_raptor_callback, 10)
        self.create_subscription(VehicleData, '/vehicle_data', self.vehicle_data_callback, 10)
        self.create_subscription(VehicleInputs, '/vehicle_inputs', self.vehicle_inputs_callback, 10)

    def powertrain_data_callback(self, msg):
        self.get_logger().info('Received PowertrainData Message')
        print(msg)

    def race_control_callback(self, msg):
        self.get_logger().info('Received RaceControl Message')
        print(msg)

    def to_raptor_callback(self, msg):
        self.get_logger().info('Received ToRaptor Message')
        print(msg)

    def vehicle_data_callback(self, msg):
        self.get_logger().info('Received VehicleData Message')
        print(msg)

    def vehicle_inputs_callback(self, msg):
        self.get_logger().info('Received VehicleInputs Message')
        print(msg)

def main(args=None):
    rclpy.init(args=args)
    msg_subscriber = DallaraInterfaceTestSubscriber()
    rclpy.spin(msg_subscriber)
    msg_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()