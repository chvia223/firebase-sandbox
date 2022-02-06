from ntpath import join
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def main():
    print("Hello World")

    db = initialize_database()

    # Used dictionary in place of a switch/case statement
    # since pre Python 3.10 doesn't support it.
    options = {
        1 : display_users,
        2 : add_user,
        3 : change_user_info,
        4 : delete_user,
    }
    while True:
        print("_______________________________")
        print("Please select one:")
        print("(1) Display Users")
        print("(2) Add User")
        print("(3) Change User Info")
        print("(4) Delete User")
        print("(5) Quit")
        print("-------------------------------")

        # Used try/except to make sure value can be an integer
        try:
            user_selection = int(input("> "))
        except ValueError:
            print("Invalid Input")
            continue

        if user_selection in range(1,5):
            options[user_selection](db)
        elif user_selection == 5:
            break
        else:
            print("Invalid Input")
            continue



def initialize_database(): 
    project_id = 'fir-sandbox-836d1'

    cred = credentials.Certificate('auth.json')
    firebase_admin.initialize_app(cred, {
        'projectId': project_id,
    })

    db = firestore.client()
    return db


def add_user(db):
    username = input("Player Name: ")

    result = db.collection('users').document(username).get()
    if result.exists:
        print("Error! User already exists in database. Perhaps you would like to make changes to their info.")
        return

    join_date = input("Join Date: ")
    auth_lvl = input("Authorization Level: ")
    base_coords = input("Base Coordinates: ")
    region_residence = input("Region Residence: ")

    db.collection('users').document(username).set({
        'joinDate' : join_date,
        'authLvl' : auth_lvl,
        'baseCoords' : base_coords,
        'regionResidence' : region_residence
    })
    print()
    print(f"Added {username} to 'Users'")

# Change specific user's information
def change_user_info(db):
    user_to_change = input("Which user's info would you like to modify: ")

    user = db.collection('users').document(user_to_change).get()
    if not user.exists:
        print()
        print("Error! User does not exist.")
        print()
        return
        
    data = user.to_dict()

    field_to_change = input("Which field would you like to modify: ")
    if field_to_change in data:
        new_value = input("Enter new value: ")
    else:
        print()
        print("Error! That field does not exist.")
        print()
        return

    db.collection('users').document(user_to_change).update({field_to_change : new_value})

    print()
    print(f"### Change Review ###\n---------------------\nUser: {user_to_change}\nField: {field_to_change}\nNew Value: {new_value}")
    print()


# Read data from Firebase
def display_users(db):
    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    for doc in docs:
        data = doc.to_dict()
        print(f"{doc.id} => {data['authLvl']}")
        print(f"|  Joined: {data['joinDate']}")
        print(f"|  Base @: {data['baseCoords']}")
        print(f"|  Region: {data['regionResidence']}")
        print()

# Will delete selected user if they exist
def delete_user(db):
    print()
    print("WARNING")
    print("This will be permananent and you will not be able to get this data back.")
    print()
    user_to_delete = input("User: ")

    result = db.collection('users').document(user_to_delete).get()
    if not result.exists:
        print("Error! User does not exist.")
        return

    print()
    confirmation = input("Are you sure you want to delete this user? (Y/n) ")
    if confirmation.lower() == 'y':
        db.collection('users').document(user_to_delete).delete()
        print(f"deleted {user_to_delete}")


main()