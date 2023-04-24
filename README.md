All commands must be executed in the project directory (``gen_query_red_made``):

### Create container:
``docker build -t db_red .``

### Run container and upload data:
``docker run -it -v /path_to_project/gen_query_red_made/volume:/volume -v /path_to_project/gen_query_red_made/data:/data db_red ./db_init.sh``

### Iterator usage:
``python iterator.py table_name batch_size shuffle``

table_name - string

batch_size - number

shuffle - True/False
Example:
``python iterator.py joined 16 True``



Iterator's response:
```
[
  [(row_1),(row_2),(row_3)...(row_BS)],
  .....,
  [(row_1),(row_2),(row_3)...(row_BS)]
]
```

### DB schema:
(foreign keys removed due to the missing docs.data)

![alt text](https://user-images.githubusercontent.com/21123064/234038422-e6a3fe0b-1160-48a8-a01e-96dfe6f86af5.png)
