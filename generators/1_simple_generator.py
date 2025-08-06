def a_simple_generator(a,b): 
    for i in range(a,b): 
        yield i 
        
        
sim_gen = a_simple_generator(1,10000000000000) 

print(next(sim_gen))
print(next(sim_gen))
print(next(sim_gen))
print(next(sim_gen))
print(next(sim_gen))
print(sim_gen)