import sqlite3
import pandas as pd
from utils import DB_PATH


class QueryGenerator():
    def __init__(self, model, table_queries, table_qrels, db_path=DB_PATH):
        self.model = model
        self.connection = sqlite3.connect(db_path)
        self.table_queries = table_queries
        self.table_qrels = table_qrels
        self.sql1 = f"delete from {self.table_queries}"
        self.sql2 = f"delete from {self.table_qrels}"
        self.connection.execute(self.sql1)
        self.connection.execute(self.sql2)

    def generate_query(self, batch, write=True):
        df_batch = pd.DataFrame(batch)
        print(df_batch.columns)
        if df_batch.shape[1] == 5:
            df_batch.rename(columns={0: 'id', 1: 'query_id', 2: 'query', 3: 'doc_id', 4: 'doc_text'}, inplace=True)
        elif df_batch.shape[1] == 3:
            df_batch.rename(columns={0: 'id', 1: 'doc_id', 2: 'doc_text'}, inplace=True)
        documents = df_batch['doc_text']
        generated_qs = []
        if 'query' in df_batch.columns:
            queries = df_batch['query']
            for doc, query in zip(documents, queries):
                generated_qs.append([query])
        else:
            pass
        if write:
            self.write_to_db(generated_qs, df_batch)
        return generated_qs

    def write_to_db(self, generated_queries, df_batch):
        queries_to_db = df_batch[['id', 'query_id']].copy()
        queries_to_db['data'] = generated_queries
        queries_to_db['data'] = queries_to_db['data'].astype('string')
        queries_to_db.to_sql(self.table_queries, self.connection, if_exists='append', index=False)
        qrels_to_db = df_batch[['id', 'query_id', 'doc_id']].copy()
        qrels_to_db.to_sql(self.table_qrels, self.connection, if_exists='append', index=False)
