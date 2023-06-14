from enum import IntEnum, Enum

from core.base_model import AbstractBaseModel, TimestampMixin
from tortoise import fields


class Status(IntEnum):
    on = 1
    off = 2

class Action(str, Enum):
    create = "create"
    delete = "delete"
    edit = "edit"


class SysUser(AbstractBaseModel, TimestampMixin):
    """
    用户表
    """
    uuid = fields.CharField(max_length=64, unique=True)
    username = fields.CharField(max_length=64, unique=True)
    password = fields.CharField(max_length=128, null=False)
    nick_name = fields.CharField(max_length=128, null=True)
    side_mode = fields.CharField(max_length=128, default='dark', description='用户侧边主题')
    header_img = fields.CharField(max_length=128, default='https://qmplusimg.henrongyi.top/gva_header.jpg',
                                  description='用户头像')
    base_color = fields.CharField(max_length=128, default='#fff', description='基础颜色')
    active_color = fields.CharField(max_length=128, default='#1890ff', description='活跃颜色')
    authority_id = fields.BigIntField(default=888, description='用户角色ID')
    phone = fields.CharField(max_length=15, null=True)
    email = fields.CharField(max_length=64, unique=True, null=True)
    enable = fields.IntEnumField(Status, default=Status.on, description='用户是否被冻结 1正常 2冻结')


    class Meta:
        table = 'sys_user'
        table_description = '用户表'
