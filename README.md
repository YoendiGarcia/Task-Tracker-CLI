# Task Tracker: CLI TODO App

## Description:

Task Tracker is a command-line interface (CLI) application designed for efficient task management. It was made as a practice of backend roadmap from roadmap.sh site. It provides a straightforward way to interact with a task database using a simple CLI interface, making it an ideal tool for both personal and professional task tracking.

## Features

Task Tracker offers a range of functionalities that enable users to manage their tasks effectively:

- **Add a Task**: Users can add a new task to their task list by providing a description. Each task is assigned a unique ID and is initially set to the "todo" status.
- **Delete a Task**: Tasks can be removed from the list by specifying their unique ID.
- **Update a Task**: The description of an existing task can be updated. This requires the task's ID and the new description.
- **List Tasks**: Users can list all tasks or filter them by status. The statuses available for filtering are "all", "done", "todo", and "in-progress".
- **Mark Task as In-Progress**: Tasks can be marked as "in-progress" by providing their ID.
- **Mark Task as Done**: Tasks can be marked as "done" by specifying their ID.

## Project Structure

- **main.py**: This is the main file containing the implementation of application. It includes:

  - `main()`: The entry point of the application that handles command-line arguments and invokes the appropriate functions.
  - `get_supported_queries()`: Returns a dictionary of supported commands and their configurations.
  - `get_querie(supported_queries: dict)`: Parses command-line arguments and returns the corresponding query function and arguments.

- **database.py**: Contains functions to interact with the data base.

  - `load_database(path: str)`: Loads the task database from a JSON file.
  - `save_database(database: dict, path: str)`: Saves the task database to a JSON file.

- **schemas**: Contains the Task schema and de Status schema

- **services**: Contains the TaskService object with the functions to handle tasks:

  - `add_task(description: str)`: Adds a new task to the database.
  - `update_task(id: int, description: str)`: Updates the description of a task.
  - `list_task(status: Status = 'all')`: Lists tasks with optional status filtering.
  - `change_status(id: int, new_status: Status)`: Change the status of a task
  - `mark_as_in_progress(id: int)`: Marks a task as "in-progress".
  - `mark_as_done(id: int)`: Marks a task as "done".
  - `delete_task(id: int)`: Deletes a task from the database.


## Installation and Usage

### **Installation**: can be done via pip

```bash
pip install git+https://github.com/YoendiGarcia/Task-Tracker-CLI
```

### **Usage**: You can now run task-tracker from command line. Here are some example

- **Add a task**

  ```bash
  $ task-tracker add "Hello word"

  ID: 1
  Description: Hello world
  Status: todo
  Created at: 2025-07-31 21:55:29.356222
  Updated at: 2025-07-31 21:55:29.356228
  -----------------------------------------
  
  ```

- **Update a task**

  ```bash
  $ task-tracker update 0 "Updated task"

  ID: 0
  Description: Updated task
  Status: todo
  Created at: 2025-07-31 21:54:32.215104
  Updated at: 2025-07-31 21:57:00.789512
  -----------------------------------------
  
  ```

- **Delete a task**

  ```bash
  $ task-tracker delete 0

  Task with ID 1 deleted
  
  ```

- **Mark as in-progress**

  ```bash
  $ task-tracker mark-in-progress 1

  ID: 1
  Description: Study python
  Status: in-progress
  Created at: 2025-07-31 22:00:23.767473
  Updated at: 2025-07-31 22:00:23.767480
  -----------------------------------------
  
  ```

- **Mark as done**

  ```bash
  $ task-tracker mark-done 1

  ID: 1
  Description: Study python
  Status: done
  Created at: 2025-07-31 22:00:23.767473
  Updated at: 2025-07-31 22:00:23.767480
  -----------------------------------------
  
  ```

- **List all tasks**

  ```bash
  $ task-tracker list

  ID: 0
  Description: Drink a coffee
  Status: todo
  Created at: 2025-07-31 22:05:47.965343
  Updated at: 2025-07-31 22:05:47.965354
  -----------------------------------------
  ID: 1
  Description: Clean the house
  Status: in-progress
  Created at: 2025-07-31 22:05:52.998571
  Updated at: 2025-07-31 22:05:52.998580
  -----------------------------------------
  ID: 2
  Description: Study python
  Status: in-progress
  Created at: 2025-07-31 22:06:04.326573
  Updated at: 2025-07-31 22:06:04.326579
  -----------------------------------------
  ID: 3
  Description: Do exercise
  Status: done
  Created at: 2025-07-31 22:06:18.859184
  Updated at: 2025-07-31 22:06:18.859190
  -----------------------------------------
  
  ```

- **List todo tasks**

  ```bash
  $ task-tracker list todo -s todo

  ID: 0
  Description: Drink a coffee
  Status: todo
  Created at: 2025-07-31 22:05:47.965343
  Updated at: 2025-07-31 22:05:47.965354
  -----------------------------------------
  
  ```

- **List in-progress tasks**

  ```bash
  $ task-tracker list -s in-progress

  ID: 1
  Description: Clean the house
  Status: in-progress
  Created at: 2025-07-31 22:05:52.998571
  Updated at: 2025-07-31 22:05:52.998580
  -----------------------------------------
  ID: 2
  Description: Study python
  Status: in-progress
  Created at: 2025-07-31 22:06:04.326573
  Updated at: 2025-07-31 22:06:04.326579
  -----------------------------------------
  
  ```

- **List done tasks**

  ```bash
  $ task-tracker list -s done

  ID: 3
  Description: Do exercise
  Status: done
  Created at: 2025-07-31 22:06:18.859184
  Updated at: 2025-07-31 22:06:18.859190
  -----------------------------------------
  
  ```
