
def lambda_handler(event, context):
    if event["status"] == "SUCCEEDED":
        print(event)
        return {"status": "SUCCEEDED", "event": event}
    else:
        print(event)
        return {"status": "FAILED", "event": event}
