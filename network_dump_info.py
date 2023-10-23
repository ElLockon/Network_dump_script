#!/bin/bash

# Function to get IP address
get_ip_address() {
    hostname -I | tr -d '[:space:]'
}

# Function to get DNS servers
get_dns_server() {
    grep '^nameserver' /etc/resolv.conf | awk '{print $2}'
}

# Function to get open ports
get_open_ports() {
    netstat -tuln | awk '/^tcp/{print $4}' | awk -F ":" '{print $NF}'
}

# Function to get network interfaces
get_network_interfaces() {
    ip addr show | grep '^[0-9]' | awk '{print $2}' | sed 's/://'
}

# Function to get the routing table
get_routing_table() {
    ip route show
}

# Function to get the ARP table
get_arp_table() {
    arp -a
}

# Get the current date and time
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# Create a filename with date and purpose
filename="network_info_$timestamp.txt"

# Save network information to a file
{
  echo "Network Information Dump"
  echo "Date and Time: $timestamp"
  echo "IP Address: $(get_ip_address)"
  echo "DNS Servers:"
  get_dns_server
  echo "Open Ports:"
  get_open_ports
  echo "Network Interfaces:"
  get_network_interfaces
  echo "Routing Table:"
  get_routing_table
  echo "ARP Table:"
  get_arp_table
} > "$filename"

# Print network information to the command line
cat "$filename"

echo "Network information has been saved to $filename"

