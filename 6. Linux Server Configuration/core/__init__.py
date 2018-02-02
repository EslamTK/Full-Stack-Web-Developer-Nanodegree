from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()

users = unit_of_work.get_users()
blogs = unit_of_work.get_blogs()
categories = unit_of_work.get_categories()

__all__ = ['unit_of_work', 'users', 'blogs', 'categories']
