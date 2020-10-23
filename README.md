AWS Serverless Architecture based Cisco DNA Demo Platform
====

Use AWS serverless architecture to build a demonstration platform for DNAC and SDWAN

Requirement 
-----
* DNA Cener 1.3.3.7
* vManager  19.2.1
* logstash
* AWS Lambda Service
* AWS Elasticsearch Service
* AWS Kibana Service V7.1.1


Descripition 
-----
Unified Programmability: Unified methodology to collect and visualize data from multiple management planes, like DNAC, ISE and vManage, to give customers a single pane of class to get all the status and statistics they wish to view.

Simplify Programmability: Face different RESTFUL API, Syslog and Netflow, provide easily programmability for developers what they need.


How it Works
-----
* Use AWS Lambda function to collection Rest API data and report file, then output to Logstash for data parsing and filtering. Finally the output data will be sent to ES/Kibana for indexing and visualization.
* Netflow, Syslog, Webhook notification data will be sent from data source directly to Logstash, without asking for Lambda function.
* Each Lambda function connect to one API interface. This flexible architecture ask for less coding and provide benefit of easing to add more functionalities. Developer only need to code for collecting data from API, all other function like Cron management, data parsing, error correlation is in charge by AWS.
* This serverless architecture does not ask for servers and database to provide service. It is easy to deploy, easy to manage, easy to develop and reduce cost by the nature of pay as running.
* Users can easily use browser to access to the platform for demo, such as data visualization result.

Demo Vision teh
-----


![alt](https://github.com/GC-Younger-Team/AWS-Serverless-Architecture-based-Cisco-DNA-Demo-Platform/blob/main/Demo_Vison.png)


Demo Topology 
-----

![alt](https://github.com/GC-Younger-Team/AWS-Serverless-Architecture-based-Cisco-DNA-Demo-Platform/blob/main/Demo_Topo.png)




Demo Show
-----
![alt](https://github.com/GC-Younger-Team/AWS-Serverless-Architecture-based-Cisco-DNA-Demo-Platform/blob/main/DNA_Demo_Visibility.png)
