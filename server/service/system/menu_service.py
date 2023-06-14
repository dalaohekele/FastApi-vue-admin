from typing import List

from model.system.menu import SysBaseMenus, SysAuthorityMenus
from service.system.user_service import get_user_authority


async def get_menus(user_id: int) -> List[dict]:
    authority_id = await get_user_authority(user_id)
    author_menus = await SysAuthorityMenus.filter(
        sys_authority_authority_id=int(authority_id)).values('sys_base_menu_id', 'sys_authority_authority_id')

    menu_id_list = []
    for author_menu in author_menus:
        menu_id_list.append(author_menu['sys_base_menu_id'])
    base_menus = await SysBaseMenus.filter(id__in=menu_id_list).order_by("sort")
    menus_map = {}
    for menus in base_menus:
        if not menus_map.__contains__(menus.parent_id):
            val = []
            val.append(menus.to_dict())
            menus_map[menus.parent_id] = val
        else:
            menus_map[menus.parent_id].append(menus.to_dict())

    menu_tree = await get_menu_tree(menus_map)
    return menu_tree


async def get_menu_tree(menus_tree: dict):
    menu_list = menus_tree["0"]
    for i in range(0, len(menu_list)):
        for keys in menus_tree:
            menu = {}
            if keys == str(menu_list[i]["ID"]):
                menu["children"] = menus_tree[keys]
                menu_list[i]["children"] = menu["children"]
    return menu_list
