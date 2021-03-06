"""
Query and deal common tables.
"""

from muddery.server.dao.base_query import BaseQuery
from muddery.server.dao.worlddata import WorldData


class DefaultSkills(object):
    """
    Character's default skills.
    """
    table_name = "default_skills"

    @classmethod
    def get(cls, character):
        """
        Get character's default skills.

        Args:
            character: (string) character's key.
        """
        return WorldData.get_table_data(cls.table_name, character=character)
