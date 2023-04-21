import sqlite3
from utils import DB_PATH


class DBIterator:
    def __init__(self, table, batch_size=1, db_path=DB_PATH):
        self.con = sqlite3.connect(db_path)
        self.table = table
        self.batch_size = batch_size
        self.cursor = self.con.cursor()
        self.min, self.max = self.cursor.execute(
            f"select min(id), max(id) from {table}"
        ).fetchall()[0]

    def __iter__(self):
        self.curr_id = self.min
        return self

    def make_request(self, start_pos, end_pos):
        sql = f"SELECT * FROM {self.table} WHERE ID BETWEEN {start_pos} and {end_pos}"
        data = self.cursor.execute(sql).fetchall()
        assert (
            len(data) == end_pos - start_pos + 1
        ), f"{len(data)} != {end_pos} - {start_pos} + 1"
        return data

    def __next__(self):
        if self.curr_id > self.max:
            raise StopIteration
        start_pos = self.curr_id
        end_pos = min(start_pos + self.batch_size - 1, self.max)
        data = self.make_request(start_pos, end_pos)
        self.curr_id += self.batch_size
        return data


if __name__ == "__main__":
    # table_name = 'docs'
    table_name = 'joined'
    bs = 1
    test_iterator = DBIterator(table_name, bs)
    for batch in test_iterator:
        print(batch)
