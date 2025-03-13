# Interior Design System

## Overview
The Interior Design System is a command-line interface (CLI) application that allows users to manage design themes, rooms, and furniture for interior design projects. It utilizes a database to store and retrieve information about various design elements.

## Features
- Add new design themes
- Add rooms with specified sizes and associated design themes
- Add furniture items to rooms
- List all rooms and furniture in the database
- Run database migrations using Alembic

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd interior-design
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   alembic upgrade head
   ```

## Usage
To run the CLI application, execute the following command:
```bash
python cli.py
```

Follow the on-screen prompts to navigate through the available options.

## License
This project is licensed under the MIT License.
