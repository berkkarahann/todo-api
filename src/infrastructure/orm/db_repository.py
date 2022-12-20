from src import db


# database model mixin for all db models to commit and
# save entities from a single source
class BaseModel:
    def commit(self):
        from sqlalchemy.exc import IntegrityError

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

    def save(self):
        db.session.add(self)
        self.commit()
        return self