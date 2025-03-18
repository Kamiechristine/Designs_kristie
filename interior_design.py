import argparse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Database Configuration (use PostgreSQL or SQLite for simplicity)
DATABASE_URL = "sqlite:///interior_design.db"  # Change to your database URL

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(Float)  # in square meters
    design_id = Column(Integer, ForeignKey('designs.id'))
    
    furniture_items = relationship("Furniture", back_populates="room")
    design = relationship("Design", back_populates="rooms")

class Furniture(Base):
    __tablename__ = 'furnitures'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    material = Column(String)
    price = Column(Float)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    
    room = relationship("Room", back_populates="furniture_items")

class Design(Base):
    __tablename__ = 'designs'
    id = Column(Integer, primary_key=True)
    theme = Column(String, nullable=False)
    
    rooms = relationship("Room", back_populates="design")

# CRUD for Room
def create_room(name, size, design_id):
    session = Session()
    new_room = Room(name=name, size=size, design_id=design_id)
    session.add(new_room)
    session.commit()
    session.close()
    print(f"Room '{name}' created successfully!")

def read_rooms():
    session = Session()
    rooms = session.query(Room).all()
    for room in rooms:
        print(room)
    session.close()

def update_room(room_id, name=None, size=None, design_id=None):
    session = Session()
    room = session.query(Room).filter(Room.id == room_id).first()
    if room:
        if name:
            room.name = name
        if size:
            room.size = size
        if design_id:
            room.design_id = design_id
        session.commit()
        print(f"Room '{room_id}' updated successfully!")
    else:
        print(f"Room '{room_id}' not found.")
    session.close()

def delete_room(room_id):
    session = Session()
    room = session.query(Room).filter(Room.id == room_id).first()
    if room:
        session.delete(room)
        session.commit()
        print(f"Room '{room_id}' deleted successfully!")
    else:
        print(f"Room '{room_id}' not found.")
    session.close()

# CRUD Operations for Furniture
def create_furniture(name, material, price, room_id):
    session = Session()
    new_furniture = Furniture(name=name, material=material, price=price, room_id=room_id)
    session.add(new_furniture)
    session.commit()
    session.close()
    print(f"Furniture '{name}' created successfully!")

def read_furniture():
    session = Session()
    furniture_list = session.query(Furniture).all()
    for furniture in furniture_list:
        print(furniture)
    session.close()

def update_furniture(furniture_id, name=None, material=None, price=None, room_id=None):
    session = Session()
    furniture = session.query(Furniture).filter(Furniture.id == furniture_id).first()
    if furniture:
        if name:
            furniture.name = name
        if material:
            furniture.material = material
        if price:
            furniture.price = price
        if room_id:
            furniture.room_id = room_id
        session.commit()
        print(f"Furniture '{furniture_id}' updated successfully!")
    else:
        print(f"Furniture '{furniture_id}' not found.")
    session.close()

def delete_furniture(furniture_id):
    session = Session()
    furniture = session.query(Furniture).filter(Furniture.id == furniture_id).first()
    if furniture:
        session.delete(furniture)
        session.commit()
        print(f"Furniture '{furniture_id}' deleted successfully!")
    else:
        print(f"Furniture '{furniture_id}' not found.")
    session.close()

# CRUD Operations for Design
def create_design(theme):
    session = Session()
    new_design = Design(theme=theme)
    session.add(new_design)
    session.commit()
    session.close()
    print(f"Design theme '{theme}' created successfully!")

def read_designs():
    session = Session()
    designs = session.query(Design).all()
    for design in designs:
        print(design)
    session.close()

def update_design(design_id, theme=None):
    session = Session()
    design = session.query(Design).filter(Design.id == design_id).first()
    if design:
        if theme:
            design.theme = theme
        session.commit()
        print(f"Design '{design_id}' updated successfully!")
    else:
        print(f"Design '{design_id}' not found.")
    session.close()

def delete_design(design_id):
    session = Session()
    design = session.query(Design).filter(Design.id == design_id).first()
    if design:
        session.delete(design)
        session.commit()
        print(f"Design '{design_id}' deleted successfully!")
    else:
        print(f"Design '{design_id}' not found.")
    session.close()

# Create all tables in the database
try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")
except Exception as e:
    print(f"Error creating database tables: {e}")
