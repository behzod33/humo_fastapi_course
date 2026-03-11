import json


JSON_FILE_PATH = 'items.json'
ENCODING = 'utf-8'


def all_items():
    with open(JSON_FILE_PATH, 'r', encoding=ENCODING) as f:
        return json.load(f)
    
    
def add_item(item_id, name, source):
    items = all_items()
    
    new_item = {
        "id": item_id, 
        "name": name, 
        "source": source
    }
    items.append(new_item)
    
    with open(JSON_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(items, f, ensure_ascii=False, indent=4)
        
    return {
        'message': 'Товар добавлен'
    }


def delete_item(item_id):
    items = all_items()
    new_items = [item for item in items if item.get("id") != item_id]
    if len(new_items) == len(items):
        return {'message': 'Товар не найден'}
    with open(JSON_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(new_items, f, ensure_ascii=False, indent=4)
    return {'message': 'Товар удалён'}


def update_item(item_id, name, source):
    items = all_items()
    for item in items:
        if item.get('id') == item_id:
            item['name'] = name
            item['source'] = source
            with open(JSON_FILE_PATH, 'w', encoding=ENCODING) as f:
                json.dump(items, f, ensure_ascii=False, indent=4)
            return {'message': 'Товар обновлён'}
    return {'message': 'Товар не найден'}


def update_delete_item(item_id, name=None, source=None, method='update'):
    items = all_items()
    found = False
    
    if method == 'update':
        for item in items:
            if item.get('id') == item_id:
                if name is not None: item['name'] = name
                if source is not None: item['source'] = source
                found = True
                break
                
    elif method == 'delete':
        initial_count = len(items)
        items = [item for item in items if item.get("id") != item_id]
        if len(items) < initial_count:
            found = True
    else:
        raise ValueError(f"Неизвестный метод: {method}")

    if not found:
        return {'message': 'Товар не найден'}

    with open(JSON_FILE_PATH, 'w', encoding=ENCODING) as f:
        json.dump(items, f, ensure_ascii=False, indent=4)
        
    return {'message': 'Товар обновлён' if method == 'update' else 'Товар удалён'}

    
    
    