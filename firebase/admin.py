import firebase_admin
from firebase_admin import db


cred_obj = firebase_admin.credentials.Certificate('./admin_cert.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://lucpc-edf35-default-rtdb.firebaseio.com/'
})

print("Menu")
print("\n1. Clear Weekly Scores")
print("2. Clear All Scores")
print("3. See number of users")

i = int(input())

if i == 1:
    ref = db.reference("/users")
    data = ref.get()
    for uid, user in data.items():
        if 'weeklyScore' in user:
            ref.child(uid).update({"weeklyScore": 0})
            print('Updated', user['name'])
        if 'problems' in user:
            problems = {}
            problems['easy'] = {'state': False, 'time': None }
            problems['medium'] = {'state': False, 'time': None }
            problems['hard'] = {'state': False, 'time': None }
            ref.child(uid).update({"problems": problems})
        
elif i == 2:
    print('Are you sure? (y/N)')
    v = input().lower()
    if v == 'n':
        exit()

    ref = db.reference("/users")
    data = ref.get()
    for uid, user in data.items():
        if 'weeklyScore' in user:
            ref.child(uid).update({"weeklyScore": 0})
        if 'totalScore' in user:
            ref.child(uid).update({"totalScore": 0})
        if 'problems' in user:
            problems = {}
            problems['easy'] = {'state': False, 'time': None }
            problems['medium'] = {'state': False, 'time': None }
            problems['hard'] = {'state': False, 'time': None }
            ref.child(uid).update({"problems": problems})
elif i == 3:
    ref = db.reference("/users")
    data = ref.get()
    print(len(data))

