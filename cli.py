# cli.py

from interior_design import create_room, read_rooms, update_room, delete_room
from interior_design import create_furniture, read_furniture, update_furniture, delete_furniture
from interior_design import create_design, read_designs, update_design, delete_design
from interior_design import create_furniture, read_furniture, update_furniture, delete_furniture
from interior_design import create_design, read_designs, update_design, delete_design

# cli.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Interior Design CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Room commands
    room_parser = subparsers.add_parser("room")
    room_subparsers = room_parser.add_subparsers(dest="action")
    
    room_create_parser = room_subparsers.add_parser("create")
    room_create_parser.add_argument("name", type=str, help="Name of the room")
    room_create_parser.add_argument("size", type=float, help="Size of the room in square meters")
    room_create_parser.add_argument("design_id", type=int, help="Design ID associated with the room")

    room_read_parser = room_subparsers.add_parser("read", help="Read all rooms")

    room_update_parser = room_subparsers.add_parser("update")
    room_update_parser.add_argument("room_id", type=int, help="ID of the room to update")
    room_update_parser.add_argument("--name", type=str, help="New name of the room")
    room_update_parser.add_argument("--size", type=float, help="New size of the room in square meters")
    room_update_parser.add_argument("--design_id", type=int, help="New design ID associated with the room")

    room_delete_parser = room_subparsers.add_parser("delete")
    room_delete_parser.add_argument("room_id", type=int, help="ID of the room to delete")

    # Furniture commands
    furniture_parser = subparsers.add_parser("furniture")
    furniture_subparsers = furniture_parser.add_subparsers(dest="action")
    
    furniture_create_parser = furniture_subparsers.add_parser("create")
    furniture_create_parser.add_argument("name", type=str, help="Name of the furniture")
    furniture_create_parser.add_argument("material", type=str, help="Material of the furniture")
    furniture_create_parser.add_argument("price", type=float, help="Price of the furniture")
    furniture_create_parser.add_argument("room_id", type=int, help="Room ID associated with the furniture")

    furniture_read_parser = furniture_subparsers.add_parser("read", help="Read all furniture")

    furniture_update_parser = furniture_subparsers.add_parser("update")
    furniture_update_parser.add_argument("furniture_id", type=int, help="ID of the furniture to update")
    furniture_update_parser.add_argument("--name", type=str, help="New name of the furniture")
    furniture_update_parser.add_argument("--material", type=str, help="New material of the furniture")
    furniture_update_parser.add_argument("--price", type=float, help="New price of the furniture")
    furniture_update_parser.add_argument("--room_id", type=int, help="New room ID associated with the furniture")

    furniture_delete_parser = furniture_subparsers.add_parser("delete")
    furniture_delete_parser.add_argument("furniture_id", type=int, help="ID of the furniture to delete")

    # Design commands
    design_parser = subparsers.add_parser("design")
    design_subparsers = design_parser.add_subparsers(dest="action")
    
    design_create_parser = design_subparsers.add_parser("create")
    design_create_parser.add_argument("theme", type=str, help="Theme of the design")

    design_read_parser = design_subparsers.add_parser("read", help="Read all designs")

    design_update_parser = design_subparsers.add_parser("update")
    design_update_parser.add_argument("design_id", type=int, help="ID of the design to update")
    design_update_parser.add_argument("--theme", type=str, help="New theme of the design")

    design_delete_parser = design_subparsers.add_parser("delete")
    design_delete_parser.add_argument("design_id", type=int, help="ID of the design to delete")

    args = parser.parse_args()

    # Handle Room commands
    if args.command == "room":
        if args.action == "create":
            create_room(args.name, args.size, args.design_id)
        elif args.action == "read":
            read_rooms()
        elif args.action == "update":
            update_room(args.room_id, args.name, args.size, args.design_id)
        elif args.action == "delete":
            delete_room(args.room_id)

    # Handle Furniture commands
    elif args.command == "furniture":
        if args.action == "create":
            create_furniture(args.name, args.material, args.price, args.room_id)
        elif args.action == "read":
            read_furniture()
        elif args.action == "update":
            update_furniture(args.furniture_id, args.name, args.material, args.price, args.room_id)
        elif args.action == "delete":
            delete_furniture(args.furniture_id)

    # Handle Design commands
    elif args.command == "design":
        if args.action == "create":
            create_design(args.theme)
        elif args.action == "read":
            read_designs()
        elif args.action == "update":
            update_design(args.design_id, args.theme)
        elif args.action == "delete":
            delete_design(args.design_id)

if __name__ == "__main__":
    main()
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
