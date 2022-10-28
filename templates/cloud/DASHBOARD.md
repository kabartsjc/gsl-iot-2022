<a name = "#arch"><img src="https://gameforge.com/de-DE/littlegames/includes/images/games/6675_5eb3e8e9456b8.jpg" alt="MYSQL" width="300"></a> 

## ⚒️ Implementing a Dashboard <a name = "dash"></a>

A set of different services compounds the cloud part of our solution. The implementation of these services follows the subsequent process:
1)	Receives all the MQTT messages from the users (through the bridge brokers) in the central broker (see [**HERE**](../mosquitto/MOSQUITTO.md) about how to configure a broker).
2)	The central broker will persist the messages in a SQL database (see [**HERE**](MYSQL.md) about how to configure the MYSQL)
3)	The dashboard will make queries in the database and fill the dashboard.

<a name = "#arch1"><img src="/fig/cloud_arch.png" alt="Cloud Basic Architecture" width="400"></a>

The dashboard supports the rescue team in identifying and prioritizing which actions are required to keep the disaster victims. In addition, the dashboard will make queries to the database (data source) and process the answer to present the information in a more helpful format.

As we told you before, the users will publish messages where the content is the id, severity, and geo-location. The **severity (SEV)** is used to calculate the **risk**, where the risk has three levels: **low, middle, or high**, where the equation to estimate is presented below.

<a name = "#risk1"><img src="/fig/risk.png" alt="Risk Calculation" width="400"></a>

The dashboard application needs to implement the minimum requirement:
-	A dynamic map where you identify the risk situation colors the node positions.
-	A dynamic map where you identify the node positions, and they are colored by the severity situation.
-	A bar chart shows the number of nodes classified by risk.
-	A bar chart shows the number of nodes classified by severity.

Two good open-source options for creating a dashboard application are **Freeboard.io** and **Grafana**. The two solutions have a cloud and premise version (our suggestion is to install the premise version, which has no restrictions). The main difference is that **Freeboard requires a JSON data source**, making it need to transform the SQL answers into this format. On the other side, **Grafana has a plugin for an MYSQL data source**.

![image](https://user-images.githubusercontent.com/26943312/197031210-ffee7b00-ca8e-47e1-bfd5-e67c23da7164.png)
-	The main page of Freboard.io is [HERE]( https://freeboard.io/).
-	The freeboard git repository is [HERE](https://github.com/Freeboard/freeboard).
-	A simplistic tutorial about installing Freeboard.io on an Ubuntu machine is [HERE]( https://installati.one/ubuntu/21.04/freeboard/).
-	A nice tutorial on how to add a data source is [HERE]( https://rafaelaroca.wordpress.com/2021/07/31/adding-data-sources-to-freeboard-is-easy/).


![image](https://user-images.githubusercontent.com/26943312/197030077-e4d2c457-a528-419c-8aed-25173242f77c.png)
* The main page of Grafana is [HERE]( https://grafana.com/).
* A complete tutorial about the foundations of Grafana is:
  * [Grafana Foundations](https://grafana.com/tutorials/grafana-fundamentals-cloud/)
  * [Basic Grafana Tutorial](https://www.sentinelone.com/blog/grafana-tutorial-detailed-guide-dashboard/)
* Good tutorials about how to configure a data source MYSQL in Grafana:
  * [Create MySQL Data Source, Collector, and Dashboard](https://sbcode.net/grafana/create-mysql-data-source/)
  * [Create a Custom MySQL Time Series Query](https://sbcode.net/grafana/custom-mysql_time_series_query/)
  * [Graphing Non-Time Series SQL Data in Grafana](https://sbcode.net/grafana/graph-non-timeseries-sql/)
  * [Using MYSQL to create a Grafana Dashboard – Video]( https://www.youtube.com/watch?v=aUq85rp7yQU)

