import redis

# ВПИШИТЕ имя контейнера Redis:
r = redis.Redis(host="____", port=6379)
message = r.get("message")
print("Message from Redis:", message.decode())
