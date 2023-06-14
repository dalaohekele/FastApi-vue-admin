import datetime
import math

from tortoise import fields
from tortoise.models import Model
from tortoise.queryset import QuerySet


class TimestampMixin:
    created_at = fields.DatetimeField(
        null=True, auto_now_add=True, description="创建时间")
    modified_at = fields.DatetimeField(
        null=True, auto_now=True, description="更新时间")
    deleted_at = fields.DatetimeField(
        null=True, description="删除时间")


class AbstractBaseModel(Model):
    id = fields.BigIntField(pk=True)

    class Meta:
        abstract = True


def paginator(query: QuerySet, page: int, page_size: int, order_by: str = "id ASC"):
    count = await query.count()
    if page < 1:
        page = 1

    if page_size <= 0:
        page_size = 10

    if page_size >= 100:
        page_size = 100

    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * page_size

    query = await query.offset(offset).limit(page_size).order_by(order_by)

    total_pages = math.ceil(count / page_size)

    paginate = {
        "total_pages": total_pages,
        "count": count,
        "current_page": page,
        "pre_page": page - 1 if page > 1 else page,
        "next_page": page if page == total_pages else page + 1
    }

    return query, paginate
