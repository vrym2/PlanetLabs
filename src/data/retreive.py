import json
from typing import List
from operator import itemgetter

class filter_data:
    """Filtering Planet data"""
    def __init__(
            self,
            planet_item_scenes_json:str = None) -> None:
        """Input Planet data item scenes JSON file"""
        self.json_file = planet_item_scenes_json
        with open(self.json_file, 'r') as f:
            self.json_data = json.load(f)
    
    def filter_with_scene_id(
            self,
            scene_id_list:List = None)-> None:
        """Filter data based on the scene ids"""
        self.items_list = [i for i in self.json_data]
        self.id_scene_indices = [index for index, scene in enumerate(self.items_list) 
                          if scene['id'] in scene_id_list]
        self.id_scenes = itemgetter(*self.id_scene_indices)(self.items_list)
        return self.id_scenes





