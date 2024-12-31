class DatabaseConnection:
    """Simulate database connection with content management."""
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        '''Establish the connection '''
        self.connected = True
        print(f"Connected to the database '{self.db_name}'.")
        return self
    
    def __exit__(self, exe_type, exe_value, traceback):
        '''Close the connection'''
        self.connected = False
        print(f"disconnected from the database '{self.db_name}'.")
        if exe_type:
            print(f"An Exception Occured: {exe_value}")
        return True
    
with DatabaseConnection("ExampleDB") as db:
    print(f"Is connected? {db.connected}")