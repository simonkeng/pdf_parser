#!/usr/bin/env bash

# Usage:
# 1. Edit the relative paths below
# 2. chmod 700 pdf_tables.sh
# 3. ./pdf_tables.sh input_file.pdf

python ~/git/scripts/users/keng/cltools/pdf_tables/pdf_table_to_dataframe.py --pdf $1
cd working/
python ~/git/scripts/users/keng/cltools/pdf_tables/pdf_table_to_dataframe.py --gs
python ~/git/scripts/users/keng/cltools/pdf_tables/pdf_table_to_dataframe.py --tess
python ~/git/scripts/users/keng/cltools/pdf_tables/pdf_table_to_dataframe.py --csv

# Optional: 

# mkdir csvs
# mv *.csv csvs/