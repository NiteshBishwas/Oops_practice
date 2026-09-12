
from opps_proj import checkbook

user1=checkbook()
print(user1.id)

checkbook.set_id(10)
user2=checkbook()
print(user2.id)