students = [['Preetha','Gayathri','Jolette','Jayanthi'],['CSE','Mech','Civil','ECE'],[1999,1999,1998,1998]]
print([[new_list[i] for new_list in students] for i in range(len(students)+1)])