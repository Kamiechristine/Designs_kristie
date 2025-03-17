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

## Contributing
If you would like to contribute to this project, please follow these guidelines:
- Ensure your code adheres to the project's coding standards.
- Submit issues for any bugs or feature requests.
- Create pull requests for proposed changes.

## Examples
Here are some examples of how to use the CLI commands:
- To add a new design theme:
  ```bash
  python cli.py add_theme "Modern"
  ```
- To list all rooms:
  ```bash
  python cli.py list_rooms
  ```

## Configuration
You can configure the application by setting environment variables or modifying the configuration files as needed.

## Troubleshooting
If you encounter issues, consider the following solutions:

### Common Issues
- **Database Connection Errors**: Ensure that your database settings are correct and that the database server is running.
- **Missing Dependencies**: If you see import errors, make sure all required packages are installed. You can install them using:
  ```bash
  pip install -r requirements.txt
  ```
- **Incorrect Command Usage**: Double-check the commands you are using. Refer to the Examples section for correct usage.

### Solutions
- **Database Connection**: Verify your database connection settings in the configuration file. Ensure that the database server is accessible.
- **Installing Dependencies**: Run the command above to install any missing packages.
- **Command Examples**: If you are unsure about the command syntax, refer to the Examples section for guidance.
- Ensure all dependencies are installed.
- Check the database connection settings.

## Contact Information
For support or inquiries, please contact the maintainers at [your-email@example.com].

## License
This project is licensed under the MIT License.
