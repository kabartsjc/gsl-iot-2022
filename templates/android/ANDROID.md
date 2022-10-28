<a name = "#arch"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsNY3BZoHFdNdUaReMN4g2Y0VLdE693oNJnXDZ4dtIL8B1IMol5fcDCIpGAyxHzF49Udo&usqp=CAU" alt="MYSQL" width="200"></a> 

## 👥 The Rescue Client <a name = "sol_desc"></a>

In this final Project, we use Android to implement our rescue app. The reason to use Android and not iPhone or other devices (like Raspberry or Arduino) is because, in this type of disaster, the most affected people are the poor, which do not have money to have an expensive device (like an iPhone) or to buy a new device (like Raspberry or Arduino).

The suggested app will send a basic MQTT message informing the user's position and severity condition. This message is intercepted by bridge brokers installed in drones flying in the affected area. An example of this interface is presented in the following Figure.


<a name = "#arch"><img src="/fig/app_new.png" alt="Rescue APP" width="200"></a>

The user will then start his app, set the **broker address and port**as his **severity**, and press the **UPDATE button**. Then, the app will send the rescue message to the broker every 10 seconds. If the changes his severity condition, the user selects the new one and presses the UPDATE button again; the app adjusts the message to the latest content and sends it to the broker. 

An example of string to be define a message in the broker is: **<ID>:<severity>:<position>**, where:
-	**ID**: is the id of node
-	**Severity**: Low||Medium||High
-	**Position**: LAT-LONG

An example of  message string is: _"node-1:Low:-23.22488,-45.232"_

**It is important to cite that the position is set manually in the code (hard) and never changed.** The reason is that in the emulator nodes, the node position uses a cartesian plane (X-Y) and requires showing the latitude and longitude positions in the dashboard. 
  
To avoid the complexity of developing the device using Android Studio, we suggest using an excellent JavaScript library named [React-Native](https://reactnative.dev/). React Native combines the best parts of native development with React, a best-in-class JavaScript library for building user interfaces. You can use React Native today in your existing Android and iOS projects or create a whole new app from scratch. As in Python, a version of an MQTT client to JavaScript – [Paho-MQTT](https://www.eclipse.org/paho/index.php?page=clients/js/index.php).

Finally, we will use an emulator (Mininet) to provide a more realistic environment. Despite Mininet supporting the emulation of an Android device, we define to do not to use it, given the complexity of integration, as the higher requirements of the host. Because this reason, the emulated victim nodes will run a Python script each simulates this situation. This script will **publish the MQTT messages** to the bridge brokers (drones).

An example of a skeleton of the JavaScript client is [**HERE**](client-android-skeleton).

An example of a publish agent in Python script is [**HERE**](mqtt_publish.py).

You can read this [**hands-on tutorial**](Android_Client_React_Native_Tutorial.pdf) which explains the skeleton JavaScript example code. 
  
You can read this [**hands-on tutorial**](../mosquitto/MQTT_Foundations.pdf) which explains the Python publish example code. 



### 📗Other References
- [A nice example of the Paho-MQTT example](https://github.com/emqx/MQTT-Client-Examples/tree/master/mqtt-client-React-Native)





