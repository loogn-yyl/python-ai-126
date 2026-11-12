"""一个通讯录能做什么: 增删查、存盘读盘。"""
import json

from .decorators import log
from .models import Contact

class AddressBook:
    def __init__(self, path: str = "contacts.json"):
        self.path = path
        self.items: dict = {}
        self.load()

    def load(self):
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.items = {}
            return
        except json.JSONDecodeError:
            print(f"数据文件损坏, 按空通讯录启动: {self.path}")
            self.items = {}
            return
        self.items = {name: Contact.from_dict(name, d) for name, d in data.items()}

    def save(self):
        data = {name: c.to_dict() for name, c in self.items.items()}
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @log
    def add(self, contact: Contact):
        if contact.name in self.items:
            raise ValueError(f"{contact.name} 已存在")
        self.items[contact.name] = contact
        self.save()
        return f"已添加 {contact.name}"

    @log
    def remove(self, name: str):
        if name not in self.items:
            raise KeyError(name)
        del self.items[name]
        self.save()
        return f"已删除 {name}"

    @log
    def find(self, keyword: str):
        return [c for c in self.items.values() if keyword in c.name or keyword in c.phone]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items.values())

class Book(AddressBook):
    def __getitem__(self, name: str):
        return self.items[name]

    def __contains__(self, name: str):
        return name in self.items

    
    def search_by_tag(self, tag):
        return [c for c in self.items.values() if tag in c.tags]

    def remove(self, name: str):
        contact = self.items[name]
        super().remove(name)
        return contact

    @log
    def find(self, keyword: str):
        return super().find(keyword)