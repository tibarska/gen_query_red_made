import os
import pandas as pd
import numpy as np

raw_dir = 'raw'
processed_dir = 'data'
if not os.path.exists(raw_dir):
    os.mkdir(raw_dir)

if not os.path.exists(processed_dir):
    os.mkdir(processed_dir)


path_raw_doc = os.path.join(raw_dir, 'docdev-stopstem.xml_1.out')
path_raw_qrels = os.path.join(raw_dir, 'msmarco-docdev-qrels.tsv')
path_raw_queries = os.path.join(raw_dir, 'queries.docdev.tsv')

path_processed_doc = os.path.join(processed_dir, 'docs.tsv')
path_processed_qrels = os.path.join(processed_dir, 'qrels.tsv')
path_processed_queries = os.path.join(processed_dir, 'queries.tsv')

df = pd.read_csv(path_raw_doc,
                 names=['query_id', 'q0', 'doc_id', 'rank', 'score', 'text'],
                 sep=' ')

docs_id = df.doc_id.unique()
df_docs = pd.DataFrame.from_records(zip(np.arange(len(docs_id)), docs_id), columns=['id', 'doc_id'])
df_docs['data'] = 'simple_text'
df_docs = df_docs[['id', 'doc_id', 'data']]
df_docs.to_csv(path_processed_doc, index=None, sep='\t', header=None)

df_qrels = pd.read_csv(path_raw_qrels, sep=' ', names=['query_id', 'rank_0', 'doc_id', 'rank_1'])
df_qrels['id'] = df_qrels.index
df_qrels = df_qrels[['id', 'query_id', 'doc_id']]
df_qrels.to_csv(path_processed_qrels, sep='\t', index=None, header=None)

df_queries = pd.read_csv(path_raw_queries, sep='\t', names=['query_id', 'data'])
df_queries['id'] = df_queries.index
df_queries = df_queries[['id', 'query_id', 'data']]
df_queries.to_csv(path_processed_queries, sep='\t', index=None, header=None)
