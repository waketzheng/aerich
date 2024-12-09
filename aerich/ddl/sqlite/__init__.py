from typing import Type

from tortoise import Model
from tortoise.backends.sqlite.schema_generator import SqliteSchemaGenerator

from aerich.ddl import BaseDDL
from aerich.exceptions import NotSupportError

ALTER_NULL_DEFAULT_COMMENT_TEMPLATE = """BEGIN TRANSACTION;
CREATE TEMPORARY TABLE "{table_name}_backup__" ({columns});
INSERT INTO "{table_name}_backup__" SELECT {columns} FROM "{table_name}";
{set_default}DROP TABLE "{table_name}";
CREATE TABLE "{table_name}" (
    {table_schema}
){extra}{comment};
INSERT INTO "{table_name}" SELECT {columns} FROM "{table_name}_backup__";
DROP TABLE "{table_name}_backup__";
COMMIT;
"""

# -------- to be delete
models_sample = """
from tortoise import Model, fields


class OneTable(Model):
   id = fields.IntField(pk=True)
   name = fields.CharField(max_length=1000, default="", null=True)
"""
set_null_sample = """
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE "onetable_backup__" ("id","name");
INSERT INTO "onetable_backup__" SELECT "id","name" FROM "onetable";
DROP TABLE "onetable";
CREATE TABLE "onetable" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(1000) DEFAULT ''
);
INSERT INTO "onetable" SELECT "id","name" FROM "onetable_backup__";
DROP TABLE "onetable_backup__";
COMMIT;
"""
add_not_null_sample = """
BEGIN TRANSACTION;
CREATE TEMPORARY TABLE onetable_backup__(id,name);
INSERT INTO onetable_backup__ SELECT id,name FROM onetable;
UPDATE onetable_backup__ SET name = '' WHERE (name IS NULL);
DROP TABLE onetable;
CREATE TABLE onetable(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(1000) NOT NULL DEFAULT ''
);
INSERT INTO onetable SELECT id,name FROM onetable_backup__;
DROP TABLE onetable_backup__;
COMMIT;
"""
# ---------------


class SqliteDDL(BaseDDL):
    schema_generator_cls = SqliteSchemaGenerator
    DIALECT = SqliteSchemaGenerator.DIALECT

    def modify_column(self, model: "Type[Model]", field_object: dict, is_pk: bool = True):
        raise NotSupportError("Modify column is unsupported in SQLite.")

    def alter_column_default(self, model: "Type[Model]", field_describe: dict):
        raise NotSupportError("Alter column default is unsupported in SQLite.")

    def alter_column_null(self, model: "Type[Model]", field_describe: dict) -> str:
        db_table = model._meta.db_table
        column = field_describe["db_column"]
        nullable = bool(field_describe.get("nullable"))
        default = field_describe.get("default") or ""  # TODO: ask user to input default
        set_default = (
            ""
            if nullable
            else f'UPDATE "{db_table}_backup__" SET "{column}" = {default!r} WHERE ("{column}" IS NULL);\n'
        )
        columns = '"id","name"'  # TODO: Get db columns by model._meta
        table_schema = """
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "name" VARCHAR(1000) DEFAULT ''
        """  # TODO
        return ALTER_NULL_DEFAULT_COMMENT_TEMPLATE.format(
            table_name=db_table,
            columns=columns,
            set_default=set_default,
            extra="",
            comment="",
            table_schema=table_schema,
        )

    def set_comment(self, model: "Type[Model]", field_describe: dict):
        raise NotSupportError("Alter column comment is unsupported in SQLite.")
