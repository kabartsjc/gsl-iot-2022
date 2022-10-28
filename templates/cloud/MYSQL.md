<a name = "#arch"><img src="https://cdn.dribbble.com/users/485324/screenshots/2522471/mysql.png" alt="MYSQL" width="300"></a> 

## ⚒️ Handling the Broker Messages <a name = "sol_desc"></a>

A set of different services compounds the cloud part of our solution. The implementation of these services follows the subsequent process:
1)	Receives all the MQTT messages from the users (through the bridge brokers) in the central broker (see [**HERE**](../mosquitto/MOSQUITTO.md) about how to configure a broker).
2)	The central broker will persist the messages in a SQL database (for example, MYSQL)
3)	The dashboard will make queries in the database and fill the dashboard (see [**HERE**](DASHBOARD.md) about how to configure a dashboard).

<a name = "#arch1"><img src="/fig/cloud_arch.png" alt="Cloud Basic Architecture" width="400"></a>

The implementation of step 2 can be pretty straightforward. A suggestion is to create a subscriber (write in Python, for example) that receives all the central broker messages about the target topic (srv/rescue) and persist them in a SQL database. This approach is shown in the following Figure, and the process happens in 4 stages:
1)	A Python client starts and subscribes to the target topic in the central broker. To provide security, this client needs to authenticate with the main broker.
2)	Central broker receives messages from the publisher’s node (emulated and real smartphones).
3)	Python client receives the messages from the central broker.
4)	Python client parses the message and persists in the SQL database using an INSERT expression.

<a name = "#arch"><img src="/fig/cloud_general.png" alt="SQL Handle Schema" width="600"></a>


An example of a MYSQL agent in Python script is [**HERE**](mysql-utils.py).

An example of a subscriber agent in Python script is [**HERE**](mqtt_subscriber.py).

You can read this [**hands-on tutorial**](../mosquitto/MQTT_Foundations.pdf) which explains the Python subscribe example code. 

If you have problems connecting the database in your Python script, you can follow this nice [**tutorial**](https://www.databasestar.com/access-denied-for-user-root-at-localhost/).


### 📗Other References
- [Very Easy Python MYSQL Tutorial - **the best**](https://www.w3schools.com/python/python_mysql_getstarted.asp)
 
- [Python and MySQL Database: A Practical Introduction](https://realpython.com/python-mysql/)




