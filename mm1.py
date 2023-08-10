import numpy as np
import matplotlib.pyplot as plt
import random

def linearCongruentialGenerator(number_of_elements:int):
  multiplier = 1
  increment = 1
  modulus = 5
  seed_value = 0
  count = number_of_elements
  number = ((multiplier * seed_value + increment)%modulus) + 1
  ans = [number]
  for i in range(1, number_of_elements):
    number = (multiplier * number + increment)%modulus + 1
    ans.append(number)
  return ans

def generateArrivalTime(inter_arrival_times: list[int]):
  start, arrival_times = 0, []
  for i in range(len(inter_arrival_times)):
    value = start + inter_arrival_times[i]
    arrival_times.append(value)
    start = value
    print("Arrival time: {:02d} hrs, {:02d} mins".format(int(0 + value//60)%24, int(value%60)))
  #print(arrival_times)
  return arrival_times

def findMetrics(arrival_times: list[int]):
  service_duration, system_idle_time, customer_wait_time = 3, 0, 0
  service_times = [arrival_times[0]]
  for i in range(1, len(arrival_times)):
    check_value = service_times[i-1] + service_duration
    original_arrival = arrival_times[i]
    service_times.append(max(check_value, original_arrival))
    if check_value > arrival_times[i]:
      customer_wait_time += abs(check_value - original_arrival)
    else:
      system_idle_time += abs(check_value - original_arrival)
  print("System idle time: {} hrs, {} mins".format(int(system_idle_time//60), int(system_idle_time%60)))
  print("Customer wait time: {}hrs, {} mins".format(int(customer_wait_time//60), int(customer_wait_time%60)))
  return (service_duration, system_idle_time, customer_wait_time)
#Random
inter_arrival_times = linearCongruentialGenerator(450)
arrival_times = generateArrivalTime(inter_arrival_times)
service_time, system_idle_time, customer_wait_time = findMetrics(arrival_times)
#Poisson
rng = np.random.default_rng()
poisson_inter_arrival = rng.poisson(4,300)
poisson_arrival_times = generateArrivalTime(poisson_inter_arrival)
poi_service_time, poi_idle_time, poi_cust_wait_time = findMetrics(poisson_arrival_times)
#Exponential
expo_inter_arrival = rng.exponential(4, 300)
expo_arrival_times = generateArrivalTime(expo_inter_arrival)
exp_service_time, exp_idle_time, exp_cust_wait_time = findMetrics(expo_arrival_times)
