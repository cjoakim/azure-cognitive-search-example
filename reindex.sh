#!/bin/bash

# Reset and Run the Indexers.
# Chris Joakim, Microsoft, 2020/09/26

source bin/activate

echo '========== reset_indexer airports'
python search-client.py reset_indexer airports

echo '========== run_indexer airports'
python search-client.py run_indexer airports

echo '========== reset_indexer documents'
python search-client.py reset_indexer documents

echo '========== run_indexer documents'
python search-client.py run_indexer documents

echo 'done'
