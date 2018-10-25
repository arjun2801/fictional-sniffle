name= raw_input('Enter your name:')
age= raw_input('Enter your age:')
c=int(age)
fname,sname=name.split(" ")
print "="*30+'\n'+ 'Hello '+ fname.upper(),sname.lower() +'\n'+'You will turn 100 in year ' + str(2018+(100-c)) +'\n'+ "="*30