import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile, QoSReliabilityPolicy


from std_msgs.msg import String

from event_camera_msgs.msg import EventPacket

class EventCamCustomSubscriber(Node):

    def __init__(self):
        super().__init__('event_cam_subscriber')
        self.get_logger().info('Demo Subscriber Node Started')

        qos = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.BEST_EFFORT)

        self.subscription = self.create_subscription(
            EventPacket,
            '/event_camera/events',
            self.listener_callback,
            qos)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        height = msg.height
        width = msg.width
        seq = msg.seq
        is_bigendian = msg.is_bigendian
        events = msg.events

        self.get_logger().info('Number of events: "%d"' % len(events), throttle_duration_sec=1.0)


def main(args=None):
    rclpy.init(args=args)

    event_cam_subscriber = EventCamCustomSubscriber()

    rclpy.spin(event_cam_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    event_cam_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()