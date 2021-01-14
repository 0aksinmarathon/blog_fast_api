from sqlalchemy import Column
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.expression import text


class TimestampMixin(object):
    created_at = Column(Timestamp, server_default=current_timestamp())
    updated_at = Column(Timestamp, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
