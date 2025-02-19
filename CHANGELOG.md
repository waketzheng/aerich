# ChangeLog

## 0.8

### [0.8.2]**(Unreleased)**

#### Added
- feat: support command `python -m aerich`. ([#417])
- feat: add --fake to upgrade/downgrade. ([#398])

#### Fixed
- fix: aerich migrate raises tortoise.exceptions.FieldError when `index.INDEX_TYPE` is not empty. ([#415])
- fix: inspectdb raise KeyError 'int2' for smallint. ([#401])
- fix: inspectdb not match data type 'DOUBLE' and 'CHAR' for MySQL. ([#187])

### Changed
- Refactored version management to use `importlib.metadata.version(__package__)` instead of hardcoded version string ([#412])

[#398]: https://github.com/tortoise/aerich/pull/398
[#401]: https://github.com/tortoise/aerich/pull/401
[#412]: https://github.com/tortoise/aerich/pull/412
[#415]: https://github.com/tortoise/aerich/pull/415
[#417]: https://github.com/tortoise/aerich/pull/417

### [0.8.1](../../releases/tag/v0.8.1) - 2024-12-27

#### Fixed
- fix: add o2o field does not create constraint when migrating. ([#396])
- Migration with duplicate renaming of columns in some cases. ([#395])
- fix: intermediate table for m2m relation not created. ([#394])
- Migrate add m2m field with custom through generate duplicated table. ([#393])
- Migrate drop the wrong m2m field when model have multi m2m fields. ([#376])
- KeyError raised when removing or renaming an existing model. ([#386])
- fix: error when there is `__init__.py` in the migration folder. ([#272])
- Setting null=false on m2m field causes migration to fail. ([#334])
- Fix NonExistentKey when running `aerich init` without `[tool]` section in config file. ([#284])
- Fix configuration file reading error when containing Chinese characters. ([#286])
- sqlite: failed to create/drop index. ([#302])
- PostgreSQL: Cannot drop constraint after deleting or rename FK on a model. ([#378])
- Fix create/drop indexes in every migration. ([#377])
- Sort m2m fields before comparing them with diff. ([#271])

#### Changed
- Allow run `aerich init-db` with empty migration directories instead of abort with warnings. ([#286])
- Add version constraint(>=0.21) for tortoise-orm. ([#388])
- Move `tomlkit` to optional and support `pip install aerich[toml]`. ([#392])

[#396]: https://github.com/tortoise/aerich/pull/396
[#395]: https://github.com/tortoise/aerich/pull/395
[#394]: https://github.com/tortoise/aerich/pull/394
[#393]: https://github.com/tortoise/aerich/pull/393
[#392]: https://github.com/tortoise/aerich/pull/392
[#388]: https://github.com/tortoise/aerich/pull/388
[#386]: https://github.com/tortoise/aerich/pull/386
[#378]: https://github.com/tortoise/aerich/pull/378
[#377]: https://github.com/tortoise/aerich/pull/377
[#376]: https://github.com/tortoise/aerich/pull/376
[#334]: https://github.com/tortoise/aerich/pull/334
[#302]: https://github.com/tortoise/aerich/pull/302
[#286]: https://github.com/tortoise/aerich/pull/286
[#284]: https://github.com/tortoise/aerich/pull/284
[#272]: https://github.com/tortoise/aerich/pull/272
[#271]: https://github.com/tortoise/aerich/pull/271

### [0.8.0](../../releases/tag/v0.8.0) - 2024-12-04

- Fix the issue of parameter concatenation when generating ORM with inspectdb (#331)
- Fix KeyError when deleting a field with unqiue=True. (#364)
- Correct the click import. (#360)
- Improve CLI help text and output. (#355)
- Fix mysql drop unique index raises OperationalError. (#346)

  **Upgrade note:**
    1. Use column name as unique key name for mysql
    2. Drop support for Python3.7

## 0.7

### [0.7.2](../../releases/tag/v0.7.2) - 2023-07-20

- Support virtual fields.
- Fix modify multiple times. (#279)
- Added `-i` and `--in-transaction` options to `aerich migrate` command. (#296)
- Fix generates two semicolons in a row. (#301)

### 0.7.1

- Fix syntax error with python3.8.10. (#265)
- Fix sql generate error. (#263)
- Fix initialize an empty database. (#267)

### 0.7.1rc1

- Fix postgres sql error (#263)

### 0.7.0

**Now aerich use `.py` file to record versions.**

Upgrade Note:

1. Drop `aerich` table
2. Delete `migrations/models` folder
3. Run `aerich init-db`

- Improve `inspectdb` adding support to `postgresql::numeric` data type
- Add support for dynamically load DDL classes easing to add support to
  new databases without changing `Migrate` class logic
- Fix decimal field change. (#246)
- Support add/remove field with index.

## 0.6

### 0.6.3

- Improve `inspectdb` and support `postgres` & `sqlite`.

### 0.6.2

- Support migration for specified index. (#203)

### 0.6.1

- Fix `pyproject.toml` not existing error. (#217)

### 0.6.0

- Change default config file from `aerich.ini` to `pyproject.toml`. (#197)

  **Upgrade note:**
    1. Run `aerich init -t config.TORTOISE_ORM`.
    2. Remove `aerich.ini`.
- Remove `pydantic` dependency. (#198)
- `inspectdb` support `DATE`. (#215)

## 0.5

### 0.5.8

- Support `indexes` change. (#193)

### 0.5.7

- Fix no module found error. (#188) (#189)

### 0.5.6

- Add `Command` class. (#148) (#141) (#123) (#106)
- Fix: migrate doesn't use source_field in unique_together. (#181)

### 0.5.5

- Fix KeyError: 'src_folder' after upgrading aerich to 0.5.4. (#176)
- Fix MySQL 5.X rename column.
- Fix `db_constraint` when fk changed. (#179)

### 0.5.4

- Fix incorrect index creation order. (#151)
- Not catch exception when import config. (#164)
- Support `drop column` for sqlite. (#40)

### 0.5.3

- Fix postgre alter null. (#142)
- Fix default function when migrate. (#147)

### 0.5.2

- Fix rename field on the field add. (#134)
- Fix postgres field type change error. (#135)
- Fix inspectdb for `FloatField`. (#138)
- Support `rename table`. (#139)

### 0.5.1

- Fix tortoise connections not being closed properly. (#120)
- Fix bug for field change. (#119)
- Fix drop model in the downgrade. (#132)

### 0.5.0

- Refactor core code, now has no limitation for everything.

## 0.4

### 0.4.4

- Fix unnecessary import. (#113)

### 0.4.3

- Replace migrations separator to sql standard comment.
- Add `inspectdb` command.

### 0.4.2

- Use `pathlib` for path resolving. (#89)
- Fix upgrade in new db. (#96)
- Fix packaging error. (#92)

### 0.4.1

- Bug fix. (#91 #93)

### 0.4.0

- Use `.sql` instead of `.json` to store version file.
- Add `rename` column support MySQL5.
- Remove callable detection for defaults. (#87)
- Fix `sqlite` stuck. (#90)

## 0.3

### 0.3.3

- Fix encoding error. (#75)
- Support multiple databases. (#68)
- Compatible with models file in directory. (#70)

### 0.3.2

- Fix migrate to new database error. (#62)

### 0.3.1

- Fix first version error.
- Fix init error. (#61)

### 0.3.0

- Refactoring migrate logic, and this version is not compatible with previous version.
- Now there don't need `old_models.py` and it store in database.
- Upgrade steps:
    1. Upgrade aerich version.
    2. Drop aerich table in database.
    3. Delete `migrations/{app}` folder and rerun `aerich init-db`.
    4. Update model and `aerich migrate` normally.

## 0.2

### 0.2.5

- Fix windows support. (#46)
- Support `db_constraint` in fk, m2m should manual define table with fk. (#52)

### 0.2.4

- Raise error with SQLite unsupported features.
- Fix Postgres alter table. (#48)
- Add `Rename` support.

### 0.2.3

- Fix tortoise ssl config.
- PostgreSQL add/drop index/unique.

### 0.2.2

- Fix postgres drop fk.
- Fix version sort.

### 0.2.1

- Fix bug in windows.
- Enhance PostgreSQL support.

### 0.2.0

- Update model file find method.
- Set `--safe` bool.

## 0.1

### 0.1.9

- Fix default_connection when upgrade
- Find default app instead of default.
- Diff MySQL ddl.
- Check tortoise config.

### 0.1.8

- Fix upgrade error when migrate.
- Fix init db sql error.
- Support change column.

### 0.1.7

- Exclude models.Aerich.
- Add init record when init-db.
- Fix version num str.

### 0.1.6

- update dependency_links

### 0.1.5

- Add sqlite and postgres support.
- Fix dependency import.
- Store versions in db.

### 0.1.4

- Fix transaction and fields import.
- Make unique index worked.
- Add cli --version.

### 0.1.3

- Support indexes and unique_together.

### 0.1.2

- Now aerich support m2m.
- Add cli cmd init-db.
- Change cli options.

### 0.1.1

- Now aerich is basic worked.
