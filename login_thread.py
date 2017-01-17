import threading
from login_action import login
from login_data import getData

data = getData()

i = 0
# print(data)
threads = []
for line in data:
    usr = line['Name']
    psw = line['Pwd']
    t = threading.Thread(target = login,args = (usr,psw,))
    threads.append(t)
    t.start()
    i += 1
print(i)







