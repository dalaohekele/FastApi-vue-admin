import logging
from typing import Union, Any

from tortoise.exceptions import DoesNotExist

from common.logger import logger
from model.system.user import SysUser


async def get_user_by_name(username: str) -> Union[SysUser, Any]:
    """
    :param username:
    :return:
    """
    try:
        user: SysUser = await SysUser.get(username=username)
    except DoesNotExist as exc:
        logger.error(exc)
        return None
    return user


async def get_user_authority(user_id: int):
    try:
        user: SysUser = await SysUser.first(user_id)
    except DoesNotExist as exc:
        logger.error(exc)
        return None
    return user.authority_id
