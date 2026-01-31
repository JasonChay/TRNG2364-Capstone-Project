# This is the pipeline driver
# it will run all the necesssary files from here

# Ingest -> Validate -> Clean -> Load -> Log -> Test
# csv_reader.py -> validation.py -> data_cleaning.py -> connection.py + loader.py -> logger.py -> tests/