# Notes for CLI

To start using postgres in Gitpod:
Type `set_pg` in the terminal and return. Followed by `psql`. If you know the name of the database you want to connect to, you can type `psql -d Insert_name` instead.

To see a list of all databases:
Type `\l` where `l` refers to list.

To create a database:
Type `CREATE DATABASE Insert_name;`.

To change to a different database:
Type `\c Insert_name_other_database` where `c` refers to connect.

To initialise/import/install a data into a database:
Type `\i Database_name.sql`.

To quit postgreSQL:
Type `\q`.

To show all tables withing a database:
Type `\dt`.

To select values from a table:
* For all values: Type `SELECT * FROM "Table_name";` and make sure to use double (not single) quotation marks followed by a semi colon.
* For only values in a specific column: Type `SELECT "Name" FROM "Table_name";`
* For specific rows which contain a certain value in a column: Type `SELECT * FROM "Table_name" WHERE "Name" = 'Alanis Morissette';` and make sure the specific value being searched for is in single quotation marks. If the searched value is an integer, single quotations are not required, but it will still work with them.

To copy into a csv file:
Type `\copy (SELECT * FROM "Table_name" WHERE "Column_name" = 'Specific_value') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;`.

To create a json file:
Type `\o test.json`.

To copy to a json file:
Type `SELECT json_agg(t) FROM (SELECT * FROM "Table_name" WHERE "Column_name" = 'Specific_value') t;`

# Notes for using Python and psycopg2 library

