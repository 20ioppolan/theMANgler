# Example Role

This is an example role. You can use this role as a guide for making your own roles. 

## Tasks

All of the ansible to execute commands and drop your malware will exist in the tasks directory, and most likely under the main.yaml file

IF you want to break your malware deploy into multiple stages, you can use:
```
- name: Use included file
  include_tasks: path/to/another/file.yaml

```
## Files

All files needed to drop your malware must go into the `files` directory. 

Make sure that the file names line up with the file names in the tasks

## Vars

Use the vars file to set paths to your artifacts. In your tasks, use the variables within a "{{}}" to assign destination paths to file copies. 

You can then, additionally, set the file path in `group_vars/all.yaml` using the same name variable, or a nested variable declaration

Example of a nested varibale declaration
```
# group_vars/all.yaml
beacons_example_role_path: "/usr/sbin/example.sh"


# within vars/main.yaml
implant_example_file_linu: "{{beacons_example_role_path}}"
```

### One extra note
Variables can go in `example-role/defaults` or `example-role/vars`. Either location while work quite well, but there are a few things to know:

1. a variable set in both locations will have the value set in `example-role/vars`. `Vars` has precedence over `defaults`. Read more about ansible varibale precedence in the ansible documentation
2. The general convention is that dynamic variables are set in variables, and static variables are set in defaults
   1. Example: the directory path of an artificat may be set the same, say /lib/security or C:\\Security, but the file name of the artifict changes every time
3. Both locations expect to find a main.yaml file in the directory
4. Either way, comment and explain your variables :) 


## Future Reading

You can look more about all of the valid directories within a role. \
Handlers may be of use if you are deploying something that causes or needs reboots. \
Default variables may be of use if you need to set a port. \
Templates may be of use if you would like to set a port with a variables. \