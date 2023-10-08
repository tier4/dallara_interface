import rclpy
from rclpy.node import Node
from autonoma_msgs.msg import PowertrainData, RaceControl, ToRaptor, VehicleData, VehicleInputs
from std_msgs.msg import Header

class DallaraInterfaceTestPublisher(Node):

    def __init__(self):
        super().__init__('msg_publisher')
        
        # Publishers for the messages
        self.powertrain_data_publisher = self.create_publisher(PowertrainData, 'powertrain_data_topic', 10)
        self.race_control_publisher = self.create_publisher(RaceControl, 'race_control_topic', 10)
        self.to_raptor_publisher = self.create_publisher(ToRaptor, 'to_raptor_topic', 10)
        self.vehicle_data_publisher = self.create_publisher(VehicleData, 'vehicle_data_topic', 10)
        self.vehicle_inputs_publisher = self.create_publisher(VehicleInputs, 'vehicle_inputs_topic', 10)
        
        timer_period = 0.1  # 10Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Create and publish each message with default values
        powertrain_data = PowertrainData()
        self.powertrain_data_publisher.publish(powertrain_data)
        
        race_control = RaceControl()
        self.race_control_publisher.publish(race_control)
        
        to_raptor = ToRaptor()
        self.to_raptor_publisher.publish(to_raptor)
        
        vehicle_data = VehicleData()
        self.vehicle_data_publisher.publish(vehicle_data)
        
        vehicle_inputs = VehicleInputs()
        self.vehicle_inputs_publisher.publish(vehicle_inputs)

        self.get_logger().info('Messages Published')

def main(args=None):
    rclpy.init(args=args)
    msg_publisher = DallaraInterfaceTestPublisher()
    rclpy.spin(msg_publisher)
    msg_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
