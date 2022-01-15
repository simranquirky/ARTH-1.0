Task: Restarting httpd service is not 'idempotence' in nature and also consumes lots of time. How to resolve this using Ansible?

Ansible provides a module, 'handlers', which can be used in the playbook to solve the challenge.

## What is Ansible Handlers?
Handlers are tasks in Ansible that, unlike other tasks, run only when notified. Handlers uses a keyword 'notify' to notify the handlers when there is any change in the part of task for which service need to be restarted. 'notify' is a pre-internal keyword in 'tasks' module and can be used anywhere or in any module in Ansible.

let’s understand the handlers as function so function run only when you call them so it creates ansible module function and run only when certain conditions are satisfied otherwise not .


Handlers takes the responsibility of the tasks means when it should execute or not .Handlers are just like regular tasks in an Ansible playbook but are only run if the Task contains a notify directive and also indicates that it changed something. For example, if a config file is changed, then the task referencing the config file templating operation may notify a service restart handler.


This means services can be bounced only if they need to be restarted. Handlers can be used for things other than service restarts, but service restarts are the most common usage.

- notify : notify keyword tells the handler to run the task only when some changes are made in the configuration file.
- Handlers in ansible to be triggered only when http configuration file changes and then handler will restart httpd service.

Ansible playbook that will configure apache httpd webserver on target nodes with the help of handlers:
```
- hosts: webserver
  tasks:
  - name: "httpd software installation"
    package:
      name: "httpd"
      state: present


  - name: "Creating web pages"
    copy:
      src: "index.html"
          dest: "/var/www/html/index.html"
    notify: restart service


  handlers:
  - name: restart service
    service:
	  name: "httpd"
	  state: restarted
	  enabled: yes
    register: restart
  - debug:
      var: restart.stdout

  - firewalld:
      port: "80/tcp"
      state: enabled
      permanent: yes
      
```
Now, as we run the playbook for the first time on a target node (consider ip 192.168.43.64) to be configured for web server, the output will be:

![img1](https://user-images.githubusercontent.com/60690997/149623104-c3337e5c-e9f8-41af-b4d4-d33c8ee2ac09.png)


You can see how handler run and performed the restart service. Here, handler run only when it gets notified by notify keyword. And notify will notify handler only when changes made in the web pages of the web service.

If we don't make any changes in the web pages, there is no need to restart the web service. Let's rerun the playbook without making any change in web pages, we will see the output as:

![img2](https://user-images.githubusercontent.com/60690997/149623147-667e70c5-0f40-4620-9301-754fe9a6cc23.png)


Yeah...!!! This time handler didn't run. So, we succeed in making restart service idempotence using Ansible..!! You can recheck again by making changes in web pages and running the playbook again.
