# interior_design.py

import argparse
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Database Configuration (use PostgreSQL or SQLite for simplicity)
DATABASE_URL = "sqlite:///interior_design.db"  # Change to your database URL

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

class Room(Base):
    """
    Room Class (representing a room in the design system)
    Attributes:
        id (int): The unique identifier for the room.
        name (str): The name of the room.
        size (float): The size of the room in square meters.
        design_id (int): The ID of the associated design theme.
    """
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(Float)  # in square meters
    design_id = Column(Integer, ForeignKey('designs.id'))
    
    furniture_items = relationship("Furniture", back_populates="room")
    design = relationship("Design", back_populates="rooms")

    def __repr__(self) -> str:
        """Return a string representation of the Room instance."""
        return f"<Room(name={self.name}, size={self.size})>"

class Furniture(Base):
    """
    Furniture Class (representing furniture in a room)
    Attributes:
        id (int): The unique identifier for the furniture.
        name (str): The name of the furniture.
        material (str): The material of the furniture.
        price (float): The price of the furniture.
        room_id (int): The ID of the associated room.
    """
    __tablename__ = 'furnitures'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    material = Column(String)
    price = Column(Float)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    
    room = relationship("Room", back_populates="furniture_items")

    def __repr__(self) -> str:
        """Return a string representation of the Furniture instance."""
        return f"<Furniture(name={self.name}, material={self.material}, price={self.price})>"

class Design(Base):
    """
    Design Class (representing a design theme)
    Attributes:
        id (int): The unique identifier for the design theme.
        theme (str): The name of the design theme.
    """
    __tablename__ = 'designs'
    id = Column(Integer, primary_key=True)
    theme = Column(String, nullable=False)
    
    rooms = relationship("Room", back_populates="design")

    def __repr__(self) -> str:
        """Return a string representation of the Design instance."""
        return f"<Design(theme={self.theme})>"

# Create all tables in the database
try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")
except Exception as e:
    print(f"Error creating database tables: {e}")
