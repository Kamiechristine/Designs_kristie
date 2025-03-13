# cli.py

import argparse
from interior_design import Room, Furniture, Design, Session

def add_design(theme):
    """Add a new design theme to the database."""
    session = Session()
    new_design = Design(theme=theme)
    session.add(new_design)
    try:
        session.commit()
        print(f"Design theme '{theme}' added successfully.")
    except Exception as e:
        print(f"Error adding design theme: {e}")
    session.close()

def add_room(name, size, design_id):
    """Add a new room to the database."""
    session = Session()
    new_room = Room(name=name, size=size, design_id=design_id)
    session.add(new_room)
    try:
        session.commit()
        print(f"Room '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding room: {e}")
    session.close()

def add_furniture(name, material, price, room_id):
    """Add a new piece of furniture to the database."""
    session = Session()
    new_furniture = Furniture(name=name, material=material, price=price, room_id=room_id)
    session.add(new_furniture)
    try:
        session.commit()
        print(f"Furniture '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding furniture: {e}")
    session.close()

def list_rooms(args):
    """List all rooms in the database."""
    session = Session()
    rooms = session.query(Room).all()
    for room in rooms:
        print(room)
    session.close()

def list_furniture(args):
    """List all furniture in the database."""
    session = Session()
    furniture_list = session.query(Furniture).all()
    for furniture in furniture_list:
        print(furniture)
    session.close()

def display_menu():
    """Display the main menu for the CLI."""
    print("\nInterior Design System CLI")
    print("1. Add Design")
    print("2. Add Room")
    print("3. Add Furniture")
    print("4. List Rooms")
    print("5. List Furniture")
    print("0. Exit")

def run_migrations():
    """Run Alembic migrations."""
    import subprocess
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Database upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during database upgrade: {e}")

def main():
    """Main function to run the CLI."""
    """Main function to run the CLI."""
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            theme = input("Enter design theme: ")
            add_design(theme)
        elif choice == '2':
            name = input("Enter room name: ")
            size_input = input("Enter room size in square meters: ")
            try:
                size = float(size_input)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the room size.")
                continue
            design_id = int(input("Enter design ID: "))
            add_room(name, size, design_id)
        elif choice == '3':
            name = input("Enter furniture name: ")
            material = input("Enter furniture material: ")
            price = float(input("Enter furniture price: "))
            room_id = int(input("Enter room ID: "))
            add_furniture(name, material, price, room_id)
        elif choice == '4':
            list_rooms(args)
        elif choice == '5':
            list_furniture()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
    parser = argparse.ArgumentParser(description="Interior Design System CLI")
    
    # Command to run migrations
    migrate_parser = subparsers.add_parser('run_migrations', help='Run Alembic migrations')
    migrate_parser.set_defaults(func=run_migrations)

    
    subparsers = parser.add_subparsers()

    # Command to add a design
    design_parser = subparsers.add_parser('add_design', help='Add a new design theme')
    design_parser.add_argument('theme', type=str, help='Design theme name')
    design_parser.set_defaults(func=add_design)

    # Command to add a room
    room_parser = subparsers.add_parser('add_room', help='Add a new room')
    room_parser.add_argument('name', type=str, help='Room name')
    room_parser.add_argument('size', type=float, help='Room size in square meters')
    room_parser.add_argument('design_id', type=int, help='Design ID associated with the room')
    room_parser.set_defaults(func=add_room)

    # Command to add furniture
    furniture_parser = subparsers.add_parser('add_furniture', help='Add furniture to a room')
    furniture_parser.add_argument('name', type=str, help='Furniture name')
    furniture_parser.add_argument('material', type=str, help='Furniture material')
    furniture_parser.add_argument('price', type=float, help='Furniture price')
    furniture_parser.add_argument('room_id', type=int, help='Room ID to place the furniture')
    furniture_parser.set_defaults(func=add_furniture)

    # Command to list rooms
    list_rooms_parser = subparsers.add_parser('list_rooms', help='List all rooms')
    list_rooms_parser.set_defaults(func=list_rooms)

    # Command to list furniture
    list_furniture_parser = subparsers.add_parser('list_furniture', help='List all furniture')
    list_furniture_parser.set_defaults(func=list_furniture)

    args = parser.parse_args()    
    args.func(args)

if __name__ == "__main__":
    main()
