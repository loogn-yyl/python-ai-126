import pytest

import contacts
from contacts import AddressBook, Contact, decorators

@pytest.fixture
def book(tmp_path, monkeypatch):
    """每次测试都拿一个干净的空通讯录, 日志写到临时目录"""
    monkeypatch.setattr(decorators, "LOG", str(tmp_path / "actions.log"))
    return AddressBook(path=str(tmp_path / "contacts.json"))

def test_正常创建():
    c = Contact("张三", "13800001111")
    assert c.name == "张三"
    assert c.email == ""
    assert c.tags == []

def test_姓名不能为空():
    with pytest.raises(ValueError):
        Contact("   ", "13800001111")

def test_电话必须11位数字():
    with pytest.raises(ValueError):
        Contact("张三", "1380000")
    with pytest.raises(ValueError):
        Contact("张三", "1380000111a")

def test_邮箱格式不对报错():
    with pytest.raises(ValueError):
        Contact("张三", "13800001111", "zs_at_example.com")
    # 邮箱为空时不校验, 这是默认值
    assert Contact("张三", "13800001111").email == ""

def test_两个实例不共享tags():
    a, b = Contact("张三", "13800001111"), Contact("李四", "13900002222")
    a.tags.append("同事")
    assert b.tags == []

def test_添加后能查到(book):
    book.add(Contact("张三", "13800001111"))
    assert len(book) == 1
    assert book.find("张")[0].name == "张三"

def test_重名报错(book):
    book.add(Contact("张三", "13800001111"))
    with pytest.raises(ValueError):
        book.add(Contact("张三", "13900002222"))

def test_存盘再读回来(book, tmp_path):
    book.add(Contact("张三", "13800001111", "zs@example.com"))
    again = AddressBook(path=str(tmp_path / "contacts.json"))
    assert len(again) == 1
    assert again.items["张三"].email == "zs@example.com"

def test_旧格式字符串能读回来(tmp_path):
    """v1 的 contacts.json 里值是纯字符串, 不是字典"""
    import json

    p = tmp_path / "old.json"
    p.write_text(json.dumps({"张三": "13800001111"}, ensure_ascii=False), encoding="utf-8")
    old = AddressBook(path=str(p))
    assert old.items["张三"].phone == "13800001111"
    assert old.items["张三"].tags == []


def test_删除(book):
    book.add(Contact("张三", "13800001111"))
    assert "已删除" in book.remove("张三")
    assert len(book) == 0

def test_删除不存在报KeyError(book):
    with pytest.raises(KeyError):
        book.remove("李四")

def test_门面只开两个东西():
    assert contacts.__all__ == ["Contact", "AddressBook"]
    assert contacts.Contact.__module__ == "contacts.models"
    assert contacts.AddressBook.__module__ == "contacts.store"

def test_按名字取值(book):
    book.add(Contact("张三", "13800001111"))
    assert book["张三"].phone == "13800001111"

def test_取不存在的人报KeyError(book):
    with pytest.raises(KeyError):
        book["李四"]

def test_in判断(book):
    book.add(Contact("张三", "13800001111"))
    assert "张三" in book
    assert "李四" not in book

def test_遍历查询(book):
    book.add(Contact("张三", "13800001111"))
    book.add(Contact("李四", "13900002222"))
    assert [c.name for c in book] == ["张三", "李四"]

def test_按标签找人(book):
    book.add(Contact("张三", "13800001111", "", ["同事"]))
    book.add(Contact("李四", "13900002222", "", ["同事", "技术部"]))
    book.add(Contact("王五", "13700003333"))
    assert [c.name for c in book.search_by_tag("同事")] == ["张三", "李四"]
    assert [c.name for c in book.search_by_tag("客户")] == []

def test_line格式():
    c = Contact("张三", "13800001111", "zs@example.com", ["同事"])
    assert c.line() == "张三 | 13800001111 | zs@example.com | 同事"
    assert Contact("李四", "13900002222").line() == "李四 | 13900002222"

def test_日志写不进去不影响业务(tmp_path, monkeypatch):
    # 指向一个不存在的目录, open() 会抛 FileNotFoundError
    monkeypatch.setattr(decorators, "LOG", str(tmp_path / "nodir" / "a.log"))
    book = AddressBook(path=str(tmp_path / "c.json"))

    # 守卫把异常吃掉了, 业务照样完成, 因为 FileNotFoundError 是 OSError 的子类
    book.add(Contact("张三", "13800001111"))
    assert len(book) == 1

    # 日志确实没写成, 连目录都没被创建出来
    assert not (tmp_path / "nodir").exists()

def test_数据文件损坏时按空通讯录启动(tmp_path, capfd):
    p = tmp_path / "bad.json"
    p.write_text("{这不是 json", encoding="utf-8")

    book = AddressBook(path=str(p))
    assert len(book) == 0

    out, _ = capfd.readouterr()
    assert "数据文件损坏" in out