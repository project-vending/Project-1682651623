
import json
from datetime import datetime

class DataProcessor:
    def __init__(self):
        self.data = {}

    def process_data(self, data):
        data = json.loads(data)
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        if data.get("source") not in self.data:
            self.data[data["source"]] = {}
        if data.get("category") not in self.data[data["source"]]:
            self.data[data["source"]][data["category"]] = []
        self.data[data["source"]][data["category"]].append((data["value"], timestamp))

    def get_data(self, source=None, category=None):
        if source is None:
            return self.data
        elif category is None:
            return self.data.get(source, {})
        else:
            return self.data.get(source, {}).get(category, [])
