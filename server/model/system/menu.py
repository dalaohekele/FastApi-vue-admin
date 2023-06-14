from tortoise import fields, Model

from core.base_model import TimestampMixin, AbstractBaseModel


class SysAuthorityMenus(Model):
    sys_base_menu_id = fields.BigIntField()
    sys_authority_authority_id = fields.BigIntField()

    class Meta:
        table = 'sys_authority_menus'
        unique_together = ('sys_base_menu_id','sys_authority_authority_id')
        table_description = '角色关联菜单'


class SysBaseMenus(TimestampMixin, AbstractBaseModel):
    menu_level = fields.BigIntField(default=0)
    parent_id = fields.CharField(max_length=64, null=True, description='父菜单ID')
    path = fields.CharField(max_length=128, null=True, description='路由path')
    name = fields.CharField(max_length=128, null=True, description='路由name')
    hidden = fields.BooleanField(default=True, null=True)
    component = fields.CharField(max_length=128, null=True, description='对应前端文件路径')
    sort = fields.BigIntField(default=0, description='排序标记')
    active_name = fields.CharField(max_length=64, null=True)
    keep_alive = fields.BooleanField(default=True, null=True)
    default_menu = fields.BooleanField(default=True, null=True)
    title = fields.CharField(max_length=64, null=True)
    icon = fields.CharField(max_length=64, null=True)
    close_tab = fields.BooleanField(default=True, null=True)

    class Meta:
        table = 'sys_base_menus'
        table_description = '角色表'

    def to_dict(self):
        return {
            "ID": self.id,
            "menuLevel": self.menu_level,
            "parentId": self.parent_id,
            "path": self.path,
            "name": self.name,
            "hidden": self.hidden,
            "component": self.component,
            "sort": self.sort,
            "meta": {"activeName": self.active_name,
                     "keepAlive": self.keep_alive,
                     "defaultMenu": self.default_menu,
                     "title": self.title,
                     "icon": self.icon,
                     "closeTab": self.close_tab,
                     }
        }
