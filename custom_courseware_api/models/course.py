""" Course DB tables """
# pylint: disable=too-few-public-methods
import uuid
from datetime import datetime
from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from ..database import Base


class CourseStatus(StrEnum):
    """ Possible Course Statuses """
    MEMBERS_ONLY = 'MEMBERS_ONLY'
    CLOSED = 'CLOSED'
    OPEN = 'OPEN'
    DELETED = 'DELETED'


class Course(Base):
    """ Course DB table """
    __tablename__ = 'courses'
    id: Mapped[uuid.UUID] = mapped_column(
        default_factory=uuid.uuid4, primary_key=True
    )
    name: Mapped[str]
    description: Mapped[str]
    last_name: Mapped[str]
    image: Mapped[str] = mapped_column(index=True)
    status: Mapped[CourseStatus] = mapped_column(default=CourseStatus.CLOSED)

    author_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    author: Mapped[str]

    admin_ids: Mapped[list[uuid.UUID]] = mapped_column(ForeignKey("users.id"))
    admins: Mapped[list[str]]

    created: Mapped[datetime] = mapped_column(
        default_factory=datetime.now, const=True
    )
    updated: Mapped[datetime] = mapped_column(
        default_factory=datetime.now, const=True
    )
