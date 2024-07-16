# Token Bucket API rate Limiter
# Mostly used by Amazon and strip to throttle their API requests
# Let's write this in python today.

#we have one predefined capacity: 5 -> this is the size of the bucket
# tokens are put into the bucket 
# rate is a preset rate if we try to add within that time frame to the 
# then you cannot add more items
# Part of my atlassian interview low level coding
# 
import time
import threading
class Bucket:
    def __init__(self,capacity,refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.last_request_time = time.time() # time now when the bucket was created
        self.tokens_left = capacity
        pass

    def refill(self):
        now = time.time()
        self.tokens_left = self.capacity
        self.last_request_time = now
        pass

    def consume(self,token): 
        now = time.time()
        remaining_time = now - self.last_request_time
        if remaining_time >= self.refill_rate:
            self.refill()
        if self.tokens_left-token >= 0:
            self.tokens_left-=token
            return True
        else:
            return False
        pass


class LeakyBucket:
    def __init__(self,capacity,leak_rate):
        self.capacity = capacity
        self.tokens_left = 0 # initial token count would be zero
        self.last_request_time = time.time()
        self.leak_rate = leak_rate
        self.start_filling()

# Bucket leaks at constant rate and process the data
    def leak(self):
        now = time.time()
        time_spent = now - self.last_request_time
        tokens_to_leak = time_spent * self.leak_rate
        self.tokens_left = max(0, self.tokens_left - tokens_to_leak)
        self.last_request_time = now
        pass
# consumer is the API requester, who is hitting the API
    def consume(self,tokens):
        if tokens < self.tokens_left:
            self.tokens_left-=tokens
            return True
        else:
            return False
        pass
    def add_token(self):
        while True:
            self.leak()
            if(self.tokens_left < self.capacity):
                self.tokens_left+=1
            time.sleep(0.5)
        pass
    def start_filling(self):
        bucket_fill = threading.Thread(target=self.add_token, daemon=True)
        bucket_fill.start()
#usage:



# rate_limiter = Bucket(capacity=5, refill_rate = 10)
# for i in range(20):
#     if rate_limiter.consume(1):
#         print("Request_sent")
#     else:
#         print("Request denied please wait")
#     time.sleep(1)


limiter = LeakyBucket(capacity=10, leak_rate= 1)  # Allow 1 token per second, with a maximum of 10 tokens
# Simulate API requests
for i in range(20):
    if limiter.consume(1):
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Denied - Rate Limit Exceeded")
    time.sleep(1)  # Simulating some delay between reqest

