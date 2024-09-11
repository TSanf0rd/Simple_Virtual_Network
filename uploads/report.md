. Which VirtualBox networking mode did you use? Why? Justify the logic. 

I used the Host-Only Adapter networking mode. This mode allows the virtual machines (VMs) to communicate with each other and with the host system while isolating them from external networks. This configuration was ideal for this assignment as it enabled direct communication between the VMs for SSH without external interference, and allowed the host machine to interact with the VMs for network troubleshooting and packet capture purposes. 

2. What did you do with the MAC addresses of the VMs when you cloned? Why? 

During the cloning process, I reinitialized the MAC addresses to assign unique MAC addresses to each VM’s network interface. This step is crucial because two machines with the same MAC address on the same network can cause conflicts, resulting in network communication issues. By ensuring unique MAC addresses, I avoided any network collisions and allowed the two VMs to communicate seamlessly on the virtual network. 

3. Include a screenshot of each of your VMs' network settings (VirtualBox and internal). Describe what the fields in your screenshot mean. 

![VM1 Network Settings](uploads/vm1_network_settings.png) ![VM2 Network Settings](uploads/vm2_network_settings.png) 

Explanation of fields: 

    Attached to: This shows the type of virtual network each VM is connected to. In this case, both are attached to the Host-Only Adapter, which allows internal communication between the VMs and the host. 

    Adapter Type: Specifies the emulated network card type. It is typically set to Intel PRO/1000 MT Desktop. 

    MAC Address: Displays the unique MAC address for each VM’s network adapter. This must be different for each machine to avoid conflicts. 

    Promiscuous Mode: Determines whether the network adapter will capture all traffic on the network or just the traffic intended for it. 

4. How did you install and configure your SSH server? 

    Installation: 

    I installed the OpenSSH server using the following command: 

    sudo dnf install openssh-server 

    Starting the SSH service: 

    After installation, I started the SSH service using 

    Sudo systemct1 start sshd.service 

What does each sub-step of installation and configuration do? 

    Installing OpenSSH Server: Downloads and installs the OpenSSH server package, which allows the system to accept SSH connections. 

    Starting SSH Service: Begins the SSH daemon (sshd), which listens for incoming SSH connections. 

6. Include screenshots of successfully SSHing from one machine to the other. 

Here’s an example of how to embed the screenshot: 

![SSH Success](uploads/ssh_success.png) 

 

 

 

 

 

 

 

 

 

 

 

 

 
