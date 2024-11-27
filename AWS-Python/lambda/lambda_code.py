import json

def calculate_square(n):
    return n ** 2

def lambda_handler(event, context):
    # Extracting the value from the event using the key "Event Name" and accessing the nested "input_number"
    event_data = event.get("Event Name")
    
    # Check if 'Event Name' exists and retrieve the data (the dictionary containing 'input_number')
    if event_data and isinstance(event_data, dict):
        n = int(event_data.get("input_number", 0))  # default to 0 if 'input_number' is missing
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing or invalid data in event.')
        }
    
    # Calculate the square
    square = calculate_square(n)
    
    # Prepare the result string
    n_square = "Square of " + str(n) + " is " + str(square)
    
    # Return the response with calculated result
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Anil from Lambda!'),
        'result': n_square
    }

# Simulating the event input (with "Event Name": "mytest" and input_number 50)
test_event = {
    "Event Name": {
        "input_number": 50
    }
}

# Now you can call the lambda_handler function with the test_event
result = lambda_handler(test_event, "test")
print(result)
