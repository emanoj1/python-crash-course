bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[2].title()}."
print(message)
print("Original list", bicycles)
bicycles[2]='BSA SLR'
print("Modified - replaced list", bicycles)
bicycles.append('99Bikes')
print("Modified - appended list", bicycles)
#index = bicycles.index('99Bikes')
#print(f"The index for 99b is", index)
bicycles[4] = 'Fuji'
print(f"New list after 99B removed",bicycles)
popped_bicycle = bicycles.pop()
print(f"The last entered item was: ", popped_bicycle)
removing_bike = 'BSA SLR'
bicycles.remove(removing_bike)
print(f"New list after delete:", bicycles)