# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]

import os
import redis
import logging

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(
            host=redis_host, port=redis_port, health_check_interval=10,
            socket_timeout=10, socket_keepalive=True,
            socket_connect_timeout=10, retry_on_timeout=True
            )

class RedisManager:
    
    def __init__(self):
        pass
    
    def is_redis_available(self):
        try:
            redis_client.ping()
            print("Successfully connected to redis")
        except (redis.exceptions.ConnectionError, ConnectionRefusedError):
            print("Redis connection error!")
            return False
        return True
    
    
    def exists(self, key):
        try:
            # key = key.encode("utf8")
            response = redis_client.exists(key)
            return response
        except Exception as e:
            print(e)
    
    def get(self, key):
        try:
            # key = key.encode("utf8")
            response = redis_client.get(key)
            return response
        except Exception as e:
            print(e)

    def set(self, key, value):
        try:
            response = redis_client.set(key, value)
            return response
        except Exception as e:
            print("error a la hora de guardar en redis")
            print(e)
    
    def sadd(self, key, value):
        return redis_client.sadd(key, value)
    
    def smembers(self, key):
        return redis_client.smembers(key)
    
    def srem(self, key, value):
        return redis_client.srem(key, value)
    
    def delete(self, key):
        return redis_client.delete(key)
    
    def keys(self):
        return redis_client.keys()
    
    def type(self, key):
        return redis_client.type(key)

    def sismember(self, key, value):
        return redis_client.sismember(key, value)
    
    def expire(self, key, seconds):
        return redis_client.expire(key, seconds)

    def get_redis_keys(self, key=None):
        try:
            print("enters get redis keys")
            matched_keys = []
            if key:
                if "*" in key:
                    keys = RedisManager().keys()
                    key = key.replace("*", "")
                    for redis_key in keys:
                        if key in redis_key.decode("utf-8"):
                            type_ = RedisManager().type(redis_key).decode("utf-8")
                            if type_ == "string":    
                                matched_keys.append((redis_key.decode("utf-8"), (RedisManager().get(redis_key)).decode("utf-8")))
                            elif type_ == "set":
                                decoded_set = set()
                                redis_set = RedisManager().smembers(redis_key)
                                for element in redis_set:
                                    try:
                                        decoded_element = element.decode("utf-8")
                                        decoded_set.add(decoded_element)
                                    except Exception as e:
                                        print(f"Error decoding element: {element}, Error: {e}")
                                matched_keys.append((redis_key.decode("utf-8"), decoded_set))
                            else:
                                matched_keys.append((redis_key.decode("utf-8"), (RedisManager().get(redis_key)).decode("utf-8")))
                    print(matched_keys)
                    return matched_keys
                if key:
                    if " " in key or "-" in key:
                        return (key, RedisManager().get(key))
                    if "phrases":
                        return (key, RedisManager().get(key))
                    return (key, RedisManager().smembers(key))
            keys = []
            for key in RedisManager().keys():
                type_ = RedisManager().type(key).decode("utf-8")
                if type_ == "string":
                    keys.append((key, RedisManager().get(key)))
                elif type_ == "set":
                    keys.append((key, RedisManager().smembers(key)))
                else:
                    keys.append((key, RedisManager().get(key)))

            return keys     
        except Exception as e:
            print("Error in get_redis_key: " + str(e))
            logging.critical("Exception in Getting Redis Keys: " + str(e))
            return []
    
    def set_redis_key(self, key, value):
        user_id = " " + key.split(" ")[-1]
        try:
            RedisManager().set(key, value)
        except Exception as e:
            logging.critical("Exception in set redis key: " + str(e))
        
    def sadd_redis_key(self, key, id, value):
        try:
            RedisManager().sadd(key, id + " " + value)
        except Exception as e:
           print("Error sadd_redis_key: " + str(e))
    def delete_redis_key(self, key):
        try:
            if len(key) > 6:
                if "*" in key:
                    keys = RedisManager().keys()
                    key = key.replace("*", "")
                    for redis_key in keys:
                        if key in redis_key.decode("utf-8"):
                            RedisManager().delete(redis_key)
            elif "*" not in key:
                RedisManager().delete(key)
        except Exception as e:
            print("Error delete_redis_key: " + e)
            
    def delete_redis_member(self, key, value):
        try:
            print("enters delete redis member")
            print(key)
            print(value)
            success = self.srem(key, value)
            if success:
                print("value '" + value + "' deleted from key '" + key + "'")
                return "value '" + value + "' deleted from key '" + key + "'"
            else:
                print("value '" + value + "' not in key '" + key + "'")
                return "value '" + value + "' not in key '" + key + "'"
        except Exception as e:
            print("Error delete_redis_member: " + e)
            