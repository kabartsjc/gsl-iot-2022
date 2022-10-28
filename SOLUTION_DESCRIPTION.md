## 💡 Solution Description <a name = "sol_desc"></a>

The problem to be answered by the Project is how to provide an efficient and secure environment to send a distress message when a natural disaster occurs (in our case, the flood disaster situation). In the scenario, there are no telecommunication links to provide essential communication (voice and data) to the rescue teams. Consequently, it is required to be innovative. It uses the means existent in the community and by volunteers, for example, [drones](https://safetymanagement.eku.edu/blog/5-ways-drones-are-being-used-for-disaster-relief/), to provide communication resources and support the identification of hazards.

<a name = "#arch"><img src="fig/architecture.png" alt="IoT Architecture" width="600"></a>

In this scenario, victims in the flood area will have a smartphone with a rescue app, which enables the citizens to send their position continuously and when they are in danger (severity level message: high, medium, or low) as a basic text message (description of their situation), as it is presented in the next Figure. To provide communication support (enabling victims’ messages to flow to the Crisis Management Center - CMC), drones flying in the crisis area intercept the message and forward it to other drones until the message arrives at the CMC. The CMC data is processed and aggregated, and a dashboard is provided for the operators to plan the rescue operation efficiently.

<a name = "#disapp"><img src="fig/app_new.png" alt="Disaster App" width="200"></a>

The approach used to implement the solution is through an Internet of Things (IoT) architecture. IoT is an [advanced automation and analytics](http://www.opjstamnar.com/download/Worksheet/Day-110/IP-XI.pdf) system that deals with artificial intelligence, sensor, networking, electronic, cloud messaging, etc., to deliver complete systems for the product or services. You use a four-stage architecture to design the solution and make it easy to understand and interoperable, as presented in the Figure below. 

<a name = "#4stage"><img src="https://miro.medium.com/max/1400/0*VmqI-3Ew1mUS5rO5.jpg" alt="4stage" width="600"></a>

A **logical view of the technical architecture** of the solution is presented below. The Emulation environment provides the core component of them. This environment is responsible for emulating a set of devices, enabling you can create many entities and providing a more realistic result for the project. To implement this environment, we recommend the use of [Mininet-WiFi](https://mininet-wifi.github.io/). Mininet-WiFi is a fork of the Mininet SDN network emulator and extended the functionality of Mininet by adding virtualized WiFi Stations and Access Points based on the standard Linux wireless drivers and the 80211_hwsim wireless simulation driver. This means that new classes have been added to support the addition of these wireless devices in a Mininet network scenario and to emulate the attributes of a mobile station, such as position and movement relative to the access points.

<a name = "#arch"><img src="fig/architecture.png" alt="IoT Architecture" width="800"></a>

There you can see two groups of nodes (emulated and real nodes). The real node is an [Android](https://developer.android.com/studio) device, which sends periodically (you need to define the period) MQTT messages to the Application Server through the bridge brokers existent in the emulation, informing the **severity and position** of the user. On the other hand, the emulated nodes are **Python scripts** with the same functionality as the real ones.

Another essential entity in this environment is the [MQTT broker](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html), implemented using [Eclipse Mosquitto](https://mosquitto.org/). Eclipse Mosquitto is an open-source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 5.0, 3.1.1, and 3.1. Mosquitto is lightweight and suitable for all devices, from low-power single-board computers to full servers. The emulation node runs in the [bridge mode](http://www.steves-internet-guide.com/mosquitto-bridge-configuration/), which means it receives the message from the user nodes and forwards them to the primary Broker, which is in the Application Server (real server located in the cloud).

There is an application server to provide the features to the Command-and-Control (C2) users. It is a real node that runs on a server box (Linux or Windows). This server has a Mosquitto broker, which receives all messages from the bridge ones and persists them in a SQL database. Also, it has a dashboard that organizes the data in a helpful format, presents the information in a map visualization, and calculates the Risk KPI (explained in the text). We suggest the use of [Freeboard.io](https://freeboard.io/) or [Grafana](https://grafana.com/oss/grafana/). Freeboard.io and Grafana are an open-source dashboard project with optional hosted subscriptions, easy to integrate with various data sources, ready for production, and very well designed. Freeboard being a dashboard, then Live Objects can serve as an API for data sources.

Finally, we use virtual interfaces in the emulation environment to enable the real and emulated nodes to exchange messages.

To better understand the architecture and how it correlates with the previous stage model, check the following figure. You can see that all user nodes represent the sensor and actuator stage; however, it is essential to cite that these nodes only send messages (they are sensors). Also, you have the gateway and edge stage. As you can see in the picture, all messages sent to the MQTT proxies are redirected directly to the cloud stage.

<a name = "#detarch"><img src="fig/detailed_arch.gif" alt="Detailed Architecture" width="600"></a>

Finally, architecture has the cloud stage. In this stage, the principal Mosquitto broker is responsible for receiving all messages from the bridge brokers (drones), converting them to SQL format, and persisting into a SQL database. Another service in the cloud is the dashboard. The suggested solution is Freeboard.io which queries the required information from the SQL database and prints them in a helpful dashboard for the rescue teams.

As we cited, the dashboard needs to present helpful information, including the geo-information about the user nodes as the classification (KPI), calculated based on the severity sent. The formula to calculate the KPI is shown, and the color code is presented in the dashboard, which you can see in the following Figure.

<a name = "#dashboard"><img src="fig/dashboard_new.png" alt="Dashboard Info" width="600"></a>

As you commented, each node sends its state using MQTT to the bridge broker. The conditions can be _low, middle, or high_; where high, the **individual is in danger**, and low, **he is safe**. The dashboard needs to compile this data and, using the formula presented in the previous figure, define the **risk situation** and **colorize** the node representation in the map.

### ➕ Support Material <a name = "sup_material"></a>

Aiming to help the students in the implementation of the final project, a set of support material were developed. Here you have the complete list with some explanations, hands-on, and examples of configuration files:
- [Client Stage - Android Device](templates/android/ANDROID.md)
- [Gateway / Edge Stage - Mosquitto Broker](templates/mosquitto/MOSQUITTO.md)
- [Cloud Stage - Python MYSQL x Mosquitto Broker Integration](templates/cloud/MYSQL.md)
- [Cloud Stage - Dashboard](templates/cloud/DASHBOARD.md)
- [Infrastructure - Mininet-Wifi](templates/mininet/MININET.md)

