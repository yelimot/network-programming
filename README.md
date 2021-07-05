# Network Programming:

This course covers all aspects of TCP/IP and network socket programming. Starting with a review of IP and TCP, including its services and IPv6, we have then learned about socket programming and time permitting, explored new trends in networking and programming.

## Homework 1 - A Time Server:

Create a simple server (single client) that can return the time and date whenever a client connects to it.
For example, it could work like this:

$ telnet 127.0.0.1  5555

connected...

It's  Apr 16 2021, Time is:  14:50:00

...disconnected..

$

That is, the server responds with date and time.. and disconnects.. See if you can create a such server.. please provide your C source code for the server and a screenshot.

## Homework 2 - Daemons everywhere!

Please revise at least 2 servers used in the previous chapters, such as multithreaded or multiprocess servers, and add daemonizing, dropping priviledges, chroot jailing, and logging to those servers.. so that they log their activities to syslog, and run as a regular user, and run chrooted to some directory.

Provide the source codes and screenshots of your servers please..

## Small project of mine:

Nontrivial client-server announcement app (you can find the report that includes detailed information about the project in the folder).
