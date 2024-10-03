# import rospy
# from std_msgs.msg import String
# import subprocess

# def callback(data):
#     text = data.data
#     rospy.loginfo(f"Received: {text}")
#     # Use espeak to vocalize the text
#     try:
#         subprocess.call(['espeak', text])
#     except Exception as e:
#         rospy.logerr(f"Failed to execute espeak: {e}")

# def elistener():
#     rospy.init_node('elistener', anonymous=True)
#     rospy.Subscriber('espeak_text', String, callback)
#     rospy.spin()

# if __name__ == '__main__':
#     try:
#         elistener()
#     except rospy.ROSInterruptException:
#         pass

# import rospy
# from std_msgs.msg import String
# import subprocess

# #def speak(text, speed=250):
#     #subprocess.run(['espeak', '-s', str(speed), test])
    
# # Callback function that will be triggered when a message is received
# def spoken_text_callback(msg):
#     rospy.loginfo(f"Received spoken text: {msg.data}")
#     #speak(msg.data, speed=250)
#     # You can process the received text here, for example, print it or perform other actions
#     print(f"Spoken text received: {msg.data}")
#     subprocess.run(['espeak', msg.data])

# # Main function to initialize the subscriber node
# def main():
#     # Initialize ROS node
#     rospy.init_node('spoken_text_listener_node')

#     # Subscriber to the 'spoken_text' topic
#     rospy.Subscriber('spoken_text', String, spoken_text_callback)

#     # Keep the node alive
#     rospy.spin()

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python
# import rospy
# from std_msgs.msg import String  # Assuming the messages are of String type
# import os
# import threading
# import queue  # Python's built-in queue module for message queuing

# # Initialize a queue with a maximum size (optional)
# message_queue = queue.Queue(maxsize=10)

# # Function to run espeak on each message from the queue
# def espeak_worker():
#     while not rospy.is_shutdown():
#         try:
#             # Get the next message from the queue (blocking call)
#             message = message_queue.get()
#             if message:
#                 # Use espeak to speak the message
#                 os.system(f'espeak "{message}"')
#                 # Mark this task as done
#                 message_queue.task_done()
#         except Exception as e:
#             rospy.logerr(f"Error in espeak_worker: {e}")

# # Callback function for the subscriber
# def callback(msg):
#     # Add the incoming message to the queue
#     try:
#         message_queue.put(msg.data, block=False)  # Non-blocking to avoid hanging
#         rospy.loginfo(f"Message added to queue: {msg.data}")
#     except queue.Full:
#         rospy.logwarn("Queue is full, dropping message!")

# def listener():
#     # Initialize the ROS node
#     rospy.init_node('espeak_subscriber', anonymous=True)

#     # Subscribe to the desired topic (assuming the topic publishes String messages)
#     rospy.Subscriber("espeak_topic", String, callback)

#     # Start the espeak worker thread
#     worker_thread = threading.Thread(target=espeak_worker)
#     worker_thread.daemon = True  # Daemonize the thread to exit with the main program
#     worker_thread.start()

#     # Spin to keep the node alive and listen for incoming messages
#     rospy.spin()

# if __name__ == '__main__':
#     try:
#         listener()
#     except rospy.ROSInterruptException:
#         pass

#!/usr/bin/env python
import rospy
from std_msgs.msg import String  # Assuming the messages are of String type
import os
import threading
import queue  # Python's built-in queue module for message queuing

# Initialize a queue with a maximum size (optional)
message_queue = queue.Queue(maxsize=10)

#os.system('espeak -s 160 "starting vocalisation")
# Function to run espeak on each message from the queue
def spoken_text():
    #os.system(f'espeak "starting vocalisation") ############################### Trying to get vocalisation for start up
    while not rospy.is_shutdown():
        try:
            # Get the next message from the queue (blocking call)
            message = message_queue.get()
            if message:
                # Use espeak to speak the message
                os.system(f'espeak -s 150 "{message}"') ######################## IF error in running voice, remove [-s 150] part from the line
                # Mark this task as done
                message_queue.task_done()
        except Exception as e:
            rospy.logerr(f"Error in espeak_worker: {e}")

# Callback function for the subscriber
def spoken_text_callback(msg):
    # Add the incoming message to the queue
    try:
        message_queue.put(msg.data, block=False)  # Non-blocking to avoid hanging
        rospy.loginfo(f"Message added to queue: {msg.data}")
    except queue.Full:
        rospy.logwarn("Queue is full, dropping message!")

def listener():
    # Initialize the ROS node
    rospy.init_node('spoken_text_listener_node', anonymous=True)

    # Subscribe to the desired topic (assuming the topic publishes String messages)
    rospy.Subscriber("spoken_text", String, spoken_text_callback)

    # Start the espeak worker thread
    worker_thread = threading.Thread(target=spoken_text)
    worker_thread.daemon = True  # Daemonize the thread to exit with the main program
    worker_thread.start()

    # Spin to keep the node alive and listen for incoming messages
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

