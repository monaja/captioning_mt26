import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Clear old data
r.delete("myqueue")

# ---- PUSH ----
r.lpush("myqueue", "task1")
r.lpush("myqueue", "task2")
r.rpush("myqueue", "task3")

print("Current list:", r.lrange("myqueue", 0, -1))

# ---- POP ----
left_item = r.lpop("myqueue")
print("LPOP:", left_item)

right_item = r.rpop("myqueue")
print("RPOP:", right_item)

print("Final list:", r.lrange("myqueue", 0, -1))

