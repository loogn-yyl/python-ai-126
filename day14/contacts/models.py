"""一个人长什么样: 字段、校验、和字典互传。只管数据, 不碰文件"""
from dataclasses import dataclass, field, asdict

@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""
    tags: list = field(default_factory=list)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("姓名不能为空")
        if not (self.phone.isdigit() and len(self.phone) == 11):
            raise ValueError(f"电话必须是 11 位数字: {self.phone}")

    def to_dict(self):
        d = asdict(self)
        d.pop("name", None)
        return d

    @classmethod
    def from_dict(cls, name: str, d):
        if isinstance(d, str):
            return cls(name, d)
        return cls(name=name, **d)

    def line(self):
        parts = [self.name, self.phone]
        if self.email:
            parts.append(self.email)
        if self.tags:
            parts.append("/".join(self.tags))
        return " | ".join(parts)

@dataclass
class StrictContact(Contact):
    def __post_init__(self):
        super().__post_init__()
        if self.email and "@" not in self.email:
            raise ValueError(f"邮箱格式不对: {self.email}")