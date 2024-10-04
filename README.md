# Migration File Generator for FluentMigrator
This Python script automates the creation of migration files for projects using **FluentMigrator in .NET.** 
# Objectives
* **Naming Convention:** Automatically generates clear and organized migration file names.

* **Time Order Management:** Ensures migration files have unique, sequential timestamps, preserving chronological order.

# Requirements
* .NET project using FluentMigrator
* Python 3.x

# Usage

Run the script from the command line, providing the name of the migration as an argument:
```bash
python migration_generator.py <MigrationName>
```

Replace ```<MigrationName>``` with a descriptive name for your migration, using PascalCase.

# Output
The script will create a new migration file in the Migrations folder with the following naming convention:

```c#
YYYYMMDDHHMMSS_MigrationName.cs
```
For Example:

```c#
20240926123456_AddUserTable.cs
```

The content will be

```c#
using FluentMigrator;

namespace YourNamespace.Migrations;

[Migration(20240926123456)]
public class _20240926123456_AddUserTable : Migration
{
    public override void Up()
    {
    }

    public override void Down()
    {
    }
}
```

# Console Output

✅ Migration file successfully created: C:\YourProject\Migrations\20240926123456_AddUserTable.cs

⚠️ Warning: Unable to determine namespace from existing files. Using default 'YourNamespace.Migrations'.

# Author
[Yusuf Başköy](https://github.com/yz-baskoy/)
