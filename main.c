#include <errno.h>
#include <fcntl.h> 
#include <string.h>
#include <serial_comm.h>
#include <socket_call.h>

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

static void set_interface_attributes(int fd, int speed, int parity);

static void set_blocking (int fd, int should_block);

socket_connect(int argc, char *argv[]);


//speed = B115200, B230400, B9600, B19200, B38400, B57600, B1200, B2400, B4800
//0 (meaning no parity), PARENB|PARODD (enable parity and use odd), PARENB (enable parity and use even), 
//PARENB|PARODD|CMSPAR (mark parity), and PARENB|CMSPAR (space parity)


