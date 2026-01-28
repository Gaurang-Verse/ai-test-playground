import os

def process_payment(user_id, amount):
    # BAD: Hardcoded token
    api_token = "sk-12345-abcdef-secret-key"
    
    # BAD: SQL Injection vulnerability
    query = f"UPDATE accounts SET balance = balance - {amount} WHERE id = '{user_id}'"
    print("Executing: " + query)
    
    # BAD: Naming convention and inefficient loop
    l = [1, 2, 3, 4, 5]
    for i in range(len(l)):
        print(l[i])

    return True
