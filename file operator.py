#================================================
# PROGRAM :- FILE OPERATOR
# PERSONAL JOURNAL MANAGER 
# BY :- HARSH PRAJAPATI 
#================================================
import os
from datetime import datetime


class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # Add a new journal entry
    def add_entry(self):
        entry = input("\nEnter your journal entry: ").strip()

        if entry == "":
            print("Entry cannot be empty.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Append mode adds entries without deleting old ones
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied.")
        except OSError as error:
            print("Error while saving entry:", error)

    # View all journal entries
    def view_entries(self):
        try:
            # Read mode reads the saved entries
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if entries.strip() == "":
                print("Your journal is empty.")
            else:
                print("\nYour Journal Entries:")
                print("--------------------------------")
                print(entries)

        except FileNotFoundError:
            print("No journal entries found. Add a new entry first.")
        except PermissionError:
            print("Error: Permission denied.")
        except OSError as error:
            print("Error while reading entries:", error)

    # Search entries by keyword or date
    def search_entries(self):
        keyword = input(
            "\nEnter a keyword or date to search: "
        ).strip()

        if keyword == "":
            print("Search text cannot be empty.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if entries.strip() == "":
                print("Your journal is empty.")
                return

            all_entries = entries.strip().split("\n\n")
            found = False

            for entry in all_entries:
                if keyword.lower() in entry.lower():
                    print("\nMatching Entry:")
                    print("--------------------------------")
                    print(entry)
                    found = True

            if not found:
                print("No entries found for:", keyword)

        except FileNotFoundError:
            print("Error: Journal file does not exist.")
        except PermissionError:
            print("Error: Permission denied.")
        except OSError as error:
            print("Error while searching:", error)

    # Delete all journal entries
    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        answer = input(
            "Are you sure you want to delete all entries? (yes/no): "
        ).strip().lower()

        if answer != "yes":
            print("Delete cancelled.")
            return

        try:
            os.remove(self.filename)
            print("All journal entries have been deleted.")

        except PermissionError:
            print("Error: Permission denied.")
        except OSError as error:
            print("Error while deleting entries:", error)

    # Create the file if it does not exist
    def create_file(self):
        try:
            # x mode creates a new file only
            with open(self.filename, "x", encoding="utf-8"):
                pass

        except FileExistsError:
            pass
        except PermissionError:
            print("Error: Cannot create journal file.")
        except OSError as error:
            print("Error:", error)

    # Display the main menu
    def show_menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:\n")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entries()

            elif choice == "4":
                self.delete_all_entries()

            elif choice == "5":
                print(
                    "Thank you for using Personal Journal Manager. "
                    "Goodbye!"
                )
                break

            else:
                print(
                    "Invalid option. Please select a valid option."
                )


# Main program
def main():
    journal = JournalManager()
    journal.create_file()
    journal.show_menu()


if __name__ == "__main__":
    main()
