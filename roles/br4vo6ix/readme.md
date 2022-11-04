# Br4vo6ix

This role is to compile and deploy Br4vo6ix automatically.

## Prerequisites

Must have the docker ansible-galaxy module installed. You can do this by running:

```shell
ansible-galaxy collection install community.docker
```

You should also have the `docker` python module installed. You can do this by running:

```shell
pip install docker
```

## Variables

```yml
---
# C2
proxy_ips:
  -  # List each of the proxy server IP's here
  -  # Ex.
  -  # 10.0.0.1
  -  # 10.0.0.2
  -  # ...
proxy_ports:
  -  # List each of the proxy ports here
  -  # Ex.
  -  # 50001
  -  # 50002
  -  # ...
server_ip: # The IP of the server which we should put the C2 server on here
xor_key: # Make up an arbitrary key here

# vvvvv MODIFY THE DETAILS BELOW vvvvv

# Windows Implant
windows_srv_name: Br4vo6ix
windows_srv_desc: Br4vo6ix Implant
windows_file_name: br4vo6ix.exe

# Linux Implant
linux_srv_name: Br4vo6ix
linux_srv_desc: Br4vo6ix Implant
linux_file_name: br4vo6ix

# FreeBSD Implant
freebsd_srv_name: Br4vo6ix
freebsd_srv_desc: Br4vo6ix Implant
freebsd_file_name: br4vo6ix

# MacOS Implant
macos_srv_name: Br4vo6ix
macos_srv_desc: Br4vo6ix Implant
macos_file_name: br4vo6ix
```

## Playbooks

Here is the recommended playbook plays for Br4vo6ix:

```yml
- name: Br4vo6ix | Compile
  hosts: localhost
  roles:
    - role: br4vo6ix
      br4vo6ix_compile: true
  tags:
    - br4vo6ix
    - compile

- name: Br4vo6ix | C2
  hosts: redteam:&172.20.1.101
  roles:
    - role: br4vo6ix
      br4vo6ix_c2_install: true
  tags:
    - br4vo6ix
    - c2

- name: Br4vo6ix | C2
  hosts: team_hosts
  roles:
    - role: br4vo6ix
      br4vo6ix_implant_install: true
  tags:
    - br4vo6ix
    - implant
```
