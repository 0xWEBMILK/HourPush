from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.logger_setup import logger

# Создание базы данных
Base = declarative_base()

class Database:
    def __init__(self, database_url: str, table_name: str):
        """Инициализация соединения с базой данных и создание таблицы."""
        self.database_url = database_url
        self.table_name = table_name

        # Создание движка SQLAlchemy
        self.engine = create_engine(self.database_url)
        
        # Настройка сессии
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        # Определение модели таблицы
        self.Task = self._create_task_model()

        # Создание таблиц
        Base.metadata.create_all(bind=self.engine)

    def _create_task_model(self):
        """Создаем модель задачи с динамическим названием таблицы."""
        class Task(Base):
            __tablename__ = self.table_name
            id = Column(Integer, primary_key=True, index=True)
            title = Column(String, nullable=False)
            lead_time = Column(Float, nullable=False)
            touch_time = Column(Float, nullable=False)
        return Task

    def save_tasks(self, tasks: list[dict], current_date):
        """Сохраняет список задач в базу данных."""
        session = self.SessionLocal()
        try:
            for task_data in tasks:
                task = self.Task(
                    month=current_date,
                    title=task_data['title'],
                    lead_time=task_data['lead_time'],
                    touch_time=task_data['touch_time']
                )
                session.add(task)
            session.commit()
            logger.info("Tasks have been successfully saved to the database.")
        except Exception as e:
            session.rollback()
            logger.error(f"Error while saving tasks to the database: {e}")
        finally:
            session.close()