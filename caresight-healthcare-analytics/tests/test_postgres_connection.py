from src.storage.postgres_loader import PostgreSQLLoader


print("Testing PostgreSQL connection")

try:
    loader = PostgreSQLLoader()

    result = loader.test_connection()

    print("Connection result:", result)

    if result:
        print("PostgreSQL connection successful.")
    else:
        print("PostgreSQL connection failed.")

except Exception as error:
    print("PostgreSQL connection failed.")
    print()
    print("ERROR:")
    print(type(error).__name__)
    print(error)