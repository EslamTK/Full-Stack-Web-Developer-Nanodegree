# Linux Server Configuration

The Project Is About Configure A Linux Server To Host A Python Flask Application.<br>

Microsoft Azure Is Used To Provide The Linux Server VM.<br>


Server Ip : 52.168.161.113<br>
SSH Port : 2200<br>
URL : http://cups.eastus.cloudapp.azure.com/<br>

grader Public Key Passphrase : **grader**<br>

**The Machine Is Currently Offline**

### Software Installed :
  * Python v3
  * Finger
  * Apache2
  * Wsgi_Mod
  * PostgreSQL
 
### Python Packages :
  * Pip3
  * sqlalchemy v1.1.10
  * oauth2client v4.1.1
  * flask v0.12.2
  
### Configurations :
  * Upgrade All The Installed Packages
  * Add User **grader** With Sudo Access And Public Key Pair Authontication
  * Enable UFW Deny All Outgoint And Allow Incoming HTTP, NTP, 2200 Ports Only
  * Install & Configure PostgreSQL: Add user (catalog, password) And Gain It Access To Catalog Database
  * Install & Configure Apache2 With The WSGI Mode To Listen On Port 80
  
### Configurations Files :
  * WSGI : https://github.com/EslamTK/Linux-Server-Configuration/blob/master/cups.wsgi
  * Apache2 : https://github.com/EslamTK/Linux-Server-Configuration/blob/master/cups.conf

### Recources Used :
  * https://docs.microsoft.com/en-us/azure/virtual-machines/linux/
  * http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
  * https://www.postgresql.org/docs/9.4/static/tutorial.html
