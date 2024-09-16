class ErrorManager:
    def __init__(self):
        self.errors = []

    def add_error(self, error_message):
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors

    def display_errors(self):
        if self.has_errors():
            print("Errors encountered during compilation:")
            for error in self.errors:
                print(error)
        else:
            print("No errors encountered.")
    
    def report_errors(self):
        if self.errors:
            for error in self.errors:
                print(f"Error: {error}")
        else:
            print("No errors found.")
