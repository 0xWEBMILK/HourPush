from sqlalchemy import create_engine

class DatabaseModel:
    def __init__(self, sqlalchemy_database_uri: str, sqlalchemy_track_modifications: bool) -> None:
        self.sqlalchemy_database_uri = sqlalchemy_database_uri
        self.sqlalchemy_track_modifications = sqlalchemy_track_modifications

    async def initialise(self) -> None:
        self.engine = create_engine(self.sqlalchemy_database_uri)

    async def write_to_table(self, dataframe, table_name: str) -> None:
        dataframe.to_sql(table_name, con=self.engine, if_exists='replace', index=False)