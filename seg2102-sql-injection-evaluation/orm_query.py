# orm_query.py
# ORM-based safe query generation (e.g., SQLAlchemy-style)

# Assume `session` is an ORM database session
# and `User` is a mapped ORM model

def get_user_by_username(session, username):
    user = session.query(User).filter_by(username=username).first()
    return user
