import numpy as np
import matplotlib.pyplot as plt
import random

def generateArrivalTime(inter_arrival_times: list[int]):
  start, arrival_times = 0, []
  for i in range(len(inter_arrival_times)):
    value = start + inter_arrival_times[i]
    arrival_times.append(value)
    start = value
    print("Arrival time: {:02d} hrs, {:02d} mins".format(int(0 + value//60)%24, int(value%60)))
  #print(arrival_times)
  return arrival_times

def findMetricsDS(arrival_times: list[int]):
  service_duration = 3
  server1_wait_time, server2_wait_time = 0, 0
  server1_end_time, server2_end_time = arrival_times[0] + service_duration, 0
  customer_wait_time = 0
  for i in range(1, len(arrival_times)):
    if server1_end_time > server2_end_time:
      if server2_end_time > arrival_times[i]:
        customer_wait_time += abs(server2_end_time - arrival_times[i])
        server2_end_time += service_duration
      else:
        server2_wait_time += abs(server2_end_time - arrival_times[i])
        server2_end_time = arrival_times[i] + service_duration
    else:
      if server1_end_time > arrival_times[i]:
        customer_wait_time += abs(server1_end_time - arrival_times[i])
        server1_end_time += service_duration
      else:
        server1_wait_time += abs(server1_end_time - arrival_times[i])
        server1_end_time = arrival_times[i] + service_duration
  print("System 1 idle time: {} hrs, {} mins".format(int(server1_wait_time//60), int(server1_wait_time%60)))
  print("System 2 idle time: {} hrs, {} mins".format(int(server2_wait_time//60), int(server2_wait_time%60)))
  print("Customer wait time: {}hrs, {} mins".format(int(customer_wait_time//60), int(customer_wait_time%60)))
  return (server1_wait_time, server2_wait_time, customer_wait_time)
#Poisson
poisson_inter_arrival = rng.poisson(4, 300)
poisson_arrival = generateArrivalTime(poisson_inter_arrival)
poi_server1_wait_time, poi_server2_wait_time, poi_customer_wait_time = findMetricsDS(poisson_arrival)
#Exponential
exponential_inter_arrival = rng.exponential(4, 300)
exponential_arrival = generateArrivalTime(exponential_inter_arrival)
exp_server1_wait_time, exp_server2_wait_time, exp_customer_wait_time = findMetricsDS(exponential_arrival)
