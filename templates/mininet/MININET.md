<a name = "#arch"><img src="https://preview.redd.it/642wajwovulz.jpg?auto=webp&s=0af1408f1571733f875ba1ecfac137e447824dbd" alt="MININET" width="500"></a> 

## 📶 The Emulation Part of the Project <a name = "sol_desc"></a>

To support the scenario description of the final project and become more realistic, we suggest using the [Mininet-Wifi](https://mininet-wifi.github.io/) project to emulate the basic network infrastructure. The basic idea is to create a set of the victim's nodes and drone networks in the emulation environment, which works like a communication relay to enable the victims to send these data to the Rescue Center. 

Unlike the real nodes, which use a [real app implementation](../android/ANDROID.md) (Android and  React-Native), the emulate ones use a Python implementation to be easiest for the node development and its integration with Mininet. 

The drone nodes are emulated. The idea is to use [Mosquitto as a bridge broker](../mosquitto/MOSQUITTO.md), forwarding all messages received from the client nodes (real or emulated ones) to the central broker in the cloud.


An example of a victim node (publish agent) in Python script is [**HERE**](../android/mqtt_publish.py).

An example of a drone node (bridge broker agent) using Mosquitto script is [**HERE**](../mosquitto/mosquitto_bridge.conf).

You can watch [**this course**](https://www.youtube.com/watch?v=0OJBGH6HVkk&t=5199s) to understand how to configure, create a scenario, and use Mininet-Wifi. The course is in Portuguese, but you can use the **caption translation** feature in Google. To learn how to use this feature, click [**HERE**](https://www.online-tech-tips.com/computer-tips/how-to-use-auto-translate-and-closed-captions-for-youtube-videos/).

[![IMAGE_ALT](https://img.youtube.com/vi/0OJBGH6HVkk/0.jpg)](https://www.youtube.com/watch?v=0OJBGH6HVkk&t=5199s)


