# Your Project Title

## Description
A brief description of your project.

## Installation
Instructions for installing the project.

## Usage
Instructions for using the project.

### CLI Functionality
The command-line interface (CLI) allows users to manage the interior design system. Below are the available commands:

- **Add Design**: 
  - Command: `add_design <theme>`
  - Description: Adds a new design theme to the database.
  - Example: `add_design "Modern"`

- **Add Room**: 
  - Command: `add_room <name> <size> <design_id>`
  - Description: Adds a new room to the database.
  - Example: `add_room "Living Room" 25.5 1`

- **Add Furniture**: 
  - Command: `add_furniture <name> <material> <price> <room_id>`
  - Description: Adds a new piece of furniture to the database.
  - Example: `add_furniture "Sofa" "Leather" 499.99 1`

- **List Rooms**: 
  - Command: `list_rooms`
  - Description: Lists all rooms in the database.

- **List Furniture**: 
  - Command: `list_furniture`
  - Description: Lists all furniture in the database.

- **Run Migrations**: 
  - Command: `run_migrations`
  - Description: Runs Alembic migrations to upgrade the database.

### Database Schema
The following classes represent the database schema for the interior design system:

- **Room Class**: Represents a room in the design system.
  - `id`: Unique identifier for the room.
  - `name`: Name of the room.
  - `size`: Size of the room in square meters.
  - `design_id`: ID of the associated design theme.

- **Furniture Class**: Represents furniture in a room.
  - `id`: Unique identifier for the furniture.
  - `name`: Name of the furniture.
  - `material`: Material of the furniture.
  - `price`: Price of the furniture.
  - `room_id`: ID of the associated room.

- **Design Class**: Represents a design theme.
  - `id`: Unique identifier for the design theme.
  - `theme`: Name of the design theme.
