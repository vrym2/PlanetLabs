import os
import json
import logging
import logging.config

# Logging file
logging.config.fileConfig('logger.ini')

def write_json_data(
        data: dict = None,
        output_dir:str = None, 
        filename:str = None):
    """Writing data into JSON file
    
    Args:
        data: Data in dictionary format
        output_dir: Directory where the file needs to be saved
        filename: Self explanatory.....
    """
    write_path = os.path.join(output_dir, filename+'.json')
    logging.info(f"Writing data into {filename}.json file")
    logging.info(f"Find the file here : {write_path}")
    with open(write_path, 'w') as f:
        json_data = json.dumps(data, indent = 4)
        f.write(json_data)
        f.close()
    logging.info("Finished!")    