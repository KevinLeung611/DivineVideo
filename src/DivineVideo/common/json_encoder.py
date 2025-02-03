import json

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return dict(obj.__dict__)
        return super().default(obj)