# seed.py

from interior_design import Session, Room, Furniture, Design

def seed_database():
    session = Session()

    # Create design themes
    modern_design = Design(theme="Modern")
    classic_design = Design(theme="Classic")
    minimalist_design = Design(theme="Minimalist")

    # Add design themes to the session
    session.add(modern_design)
    session.add(classic_design)
    session.add(minimalist_design)

    # Commit the designs to the database
    try:
        session.commit()
        print("Design themes added successfully!")
    except Exception as e:
        print(f"Error adding design themes: {e}")

    # Create rooms and associate them with design themes
    living_room = Room(name="Living Room", size=25.5, design_id=modern_design.id) if modern_design.id else None
    bedroom = Room(name="Bedroom", size=18.2, design_id=classic_design.id) if classic_design.id else None
    kitchen = Room(name="Kitchen", size=15.0, design_id=minimalist_design.id) if minimalist_design.id else None

    # Add rooms to the session
    session.add(living_room)
    session.add(bedroom)
    session.add(kitchen)

    # Commit rooms to the database
    try:
        session.commit()
        print("Rooms added successfully!")
    except Exception as e:
        print(f"Error adding rooms: {e}")

    # Create furniture items and associate them with rooms
    sofa = Furniture(name="Sofa", material="Leather", price=800.0, room_id=living_room.id)
    coffee_table = Furniture(name="Coffee Table", material="Wood", price=150.0, room_id=living_room.id)
    bed = Furniture(name="Bed", material="Wood", price=600.0, room_id=bedroom.id)
    dining_table = Furniture(name="Dining Table", material="Marble", price=1200.0, room_id=kitchen.id)
    refrigerator = Furniture(name="Refrigerator", material="Stainless Steel", price=1000.0, room_id=kitchen.id)

    # Add furniture items to the session
    session.add(sofa)
    session.add(coffee_table)
    session.add(bed)
    session.add(dining_table)
    session.add(refrigerator)

    # Commit furniture to the database
    try:
        session.commit()
        print("Furniture added successfully!")
    except Exception as e:
        print(f"Error adding furniture: {e}")

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
