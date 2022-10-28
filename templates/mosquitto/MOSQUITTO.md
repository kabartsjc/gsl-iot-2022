<a name = "#arch"><img src="https://user-images.githubusercontent.com/26943312/196437591-9a485ca2-9459-4009-9cc2-e80328f7adee.gif" alt="MQTT Broker Architecture" width="300"></a> 

## 💡 What is Eclipse Mosquitto <a name = "sol_desc"></a>

**MQTT protocol** is a Machine to Machine (M2M) protocol widely used in IoT (Internet of things). The MQTT protocol is a message-based, extraordinarily lightweight protocol, so it is adopted in IoT. Almost all IoT platforms support MQTT to send and receive data from smart objects. The MQTT IoT protocol was developed around 1999. The main goal of this protocol was to create a very efficient protocol from the bandwidth point of view. Moreover, it is a very power-saving protocol. For all these reasons, it is suitable for IoT.

This uses the publish-subscribe paradigm in contrast to HTTP based on the request/response paradigm. It uses binary messages to exchange information with low overhead. It is straightforward to implement, and it is open. All these aspects contribute to its extensive adoption in IoT. Another exciting part is that the MQTT protocol uses a TCP stack as a transmission substrate.

The **critical component in MQTT is the broker**. The main task of the MQTT broker is dispatching messages to the MQTT clients (“subscribers”). In other words, the MQTT broker receives messages from the publisher and dispatches these messages to the subscribers. While it dispatches messages, the MQTT broker uses the topic to filter the MQTT clients that will receive the news. The topic is a string, and it is possible to combine the topics creating topic levels. A topic is a virtual channel that connects a publisher to its subscribers. MQTT broker manages this topic. Through this virtual channel, the publisher is decoupled from the subscribers, and the MQTT clients (publishers or subscribers) do not have to know each other to exchange data. This makes this protocol highly scalable without a direct dependency on the message producer (“publisher”) and the message consumer (“subscriber”).

<a name = "#arch"><img src="https://www.bivocom.com/wp-content/uploads/2021/03/MQTT_Schema_EN.jpg" alt="MQTT Broker Architecture" width="600"></a>

[Eclipse Mosquitto](https://mosquitto.org/) is an open-source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 5.0, 3.1.1, and 3.1.It is lightweight and suitable for all devices, from low-power single-board computers to full servers. 

Mosquitto, in our project, will be used in two different nodes. The first one is in the emulated drones, which receive the “publish” messages from the Android devices and send them to the primary broker, which is installed in the cloud (or where the C2 services are deployed). So in the emulated drones, Mosquitto needs to work as a bridge broker. 

Mosquitto has a bridging feature that lets you connect two (or more) brokers. They are generally used for sharing messages between systems. Typical usage is connected edge MQTT brokers to a central or remote MQTT network. So naturally, the edge bridge will only bridge a subset of the local MQTT traffic. This behavior is shown in the following Figure.

<a name = "#arch"><img src="https://miro.medium.com/max/902/1*_-2hDG1tsjDkgizilchSgg.png" alt="Mosquitto Bridge Broker Architecture" width="600"></a>

Finally, given the limitation of the JavaScript MQTT client library, which does not correctly send messages to Mosquitto, it is required to use the **WebSocket protocol**. WebSocket provides full-duplex communication channels over a single TCP/IP connection, closely associated with HTTP, as it uses HTTP for the initial connection establishment. MQTT over WebSocket allows you to receive MQTT data directly into a web browser. This is important as the web browser may become the DE-facto interface for displaying MQTT data. The JavaScript client provides MQTT WebSocket support for web browsers.

An example of a configuration file to use Mosquitto as a central broker is [**HERE**](mosquitto_central.conf).

An example of a configuration file to use Mosquitto as a bridge broker is [**HERE**](mosquitto_bridge.conf).

You can read a hands-on tutorial about configuring Mosquitto in a similar scenario used in this final project [**HERE**](MQTT_Foundations.pdf).

### 📗Other References
- [MQTT for Beginners Tutorials and Course](http://www.steves-internet-guide.com/mqtt-basics-course/)
 
- [IoT con MQTT + Mosquitto + Python - ES](https://www.youtube.com/watch?v=hEFSaysEIhs)




