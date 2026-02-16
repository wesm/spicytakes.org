---
title: "Accessing Dell Server Remotely Using iDRac"
date: 2024-01-10
url: https://blog.mempko.com/accessing-dell-server-remotely-using-idrac/
word_count: 255
---

kg-card-begin: html

Do you need to access a Dell server remotely using iDRac outside it’s intranet? iDRac, or Integrated Dell Remote Access Controller, is a powerful tool that allows for remote management. It uses a dedicated IP and operates through a web interface on HTTPS (port 443).


Here’s a step-by-step guide to set up remote access:


**Create an SSH Tunnel:**


First, establish an SSH tunnel to a machine you have access to. This can be done using the following


```
ssh -L 8443:<iDRac IP>:443 -L 5900:<iDRac IP>:5900 -L 5901:<iDRac IP>:5901 my@publicmachine.com
```


This command maps port 8443 on your local machine to port 443 on the iDRac server (and similar mappings for ports 5900 and 5901, which are often used for virtual console access).


**Troubleshooting the 400 Error:**


If you attempt to connect through your local browser using `https://localhost:8443`, you might receive a 400 error. This occurs because iDRac redirects using its IP address. To resolve this, you need to redirect traffic from the iDRac IP to your localhost.


Execute the following command:


```
sudo iptables -t nat -A OUTPUT -d <iDRac IP> -j DNAT --to-destination 127.0.0.1
```


Replace with the actual IP address of your iDRac.


**Accessing iDRac:**


Finally, navigate to `https://<iDRac IP>:8443` in your browser. This should successfully redirect and allow you access to the iDRac interface.


---


Remember, remote server management can be complex and might require specific network configurations based on your organization’s setup. Always ensure you have the necessary permissions and understand the security implications of remote access.

kg-card-end: html