from pymongo import MongoClient

def main():
    try:
        # Connect to local MongoDB
        client = MongoClient("mongodb://localhost:27017/")

        # Test DB & collection
        db = client["test_db"]
        collection = db["test_collection"]

        # Insert test data
        test_doc = {"name": "DJ", "role": "MLOps Engineer", "status": "MongoDB OK"}
        result = collection.insert_one(test_doc)

        print("Inserted document ID:", result.inserted_id)

        # Read it back
        fetched = collection.find_one({"_id": result.inserted_id})
        print("Fetched document:", fetched)

        print("\nMongoDB is working successfully ✔️")
        print("All documents:")
        for d in collection.find():
            print(d)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

