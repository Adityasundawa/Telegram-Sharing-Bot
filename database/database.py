#(©)CodeXBotz

import datetime
import pymongo, os
from config import DB_URI, DB_NAME, DAILY_LIMIT_NEW_USER, DAILY_LIMIT_RESET


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']


async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)


async def add_user(user_id: int, username):
    current_date = datetime.date.today()
    user_data.insert_one({
        '_id': user_id,
        'username': username,
        'user_premium': 'no',          # "no" = non-premium, "yes" = premium
        'join_date': current_date.strftime("%Y-%m-%d"),
        'new_user': 'yes',
        'last_access': current_date.strftime("%Y-%m-%d"),
        'daily_limit': DAILY_LIMIT_NEW_USER,   # ← dari .env
    })
    return


async def reset_daily_limit(user_id: int):
    try:
        current_date = datetime.date.today()
        result = user_data.update_one(
            {"_id": user_id},
            {"$set": {
                "last_access": current_date.strftime("%Y-%m-%d"),
                "daily_limit": DAILY_LIMIT_RESET    # ← dari .env
            }}
        )
        if result.matched_count == 1:
            return True
        else:
            return False
    except Exception as e:
        return False


async def decrease_daily_limit(user_id: int):
    try:
        user = user_data.find_one({"_id": user_id})
        if user:
            current_limit = user.get("daily_limit", 0)
            if current_limit > 0:
                new_limit = current_limit - 1
                user_data.update_one({"_id": user_id}, {"$set": {"daily_limit": new_limit}})
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False


async def update_new_user(user_id: int):
    try:
        result = user_data.update_one(
            {"_id": user_id},
            {"$set": {"new_user": "no"}}
        )
        if result.matched_count == 1:
            return True
        else:
            return False
    except Exception as e:
        return False


async def find_user(user_id: int):
    result = user_data.find_one({"_id": user_id})
    if result:
        result = {
            '_id': result['_id'],
            'username': result['username'],
            'user_premium': result['user_premium'],
            'join_date': result['join_date'],
            'last_access': result['last_access'],
            'new_user': result['new_user'],
            'daily_limit': result['daily_limit']
        }
    else:
        result = {"status": "Not Found"}
    return result


async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
    return user_ids


async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return