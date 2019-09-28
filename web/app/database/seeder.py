from app.main import create_app
from app.config import BaseConfig
from .db import db
from .models import (
  UserRole, UserPermission, user_role_permission,
  ReviewStatusKind
)

def main():
  app = create_app(BaseConfig)
  with app.app_context():
    role_contributer = UserRole(name='contributer')
    role_reviewer = UserRole(name='reviewer')
    role_admin = UserRole(name='admin')
  
    perm_contributer = UserPermission(name='contributer')
    perm_reviewer = UserPermission(name='reviewer')
    perm_admin = UserPermission(name='admin')

    role_contributer.permission.append(perm_contributer)

    role_reviewer.permission.append(perm_contributer)
    role_reviewer.permission.append(perm_reviewer)

    role_admin.permission.append(perm_contributer)
    role_admin.permission.append(perm_reviewer)
    role_admin.permission.append(perm_admin)

    review_status_kinds = [
      ReviewStatusKind(name='pending'),
      ReviewStatusKind(name='rejected'),
      ReviewStatusKind(name='approved'),
    ]

    db.session.bulk_save_objects([
      role_contributer,
      role_reviewer,
      role_admin,
      perm_contributer,
      perm_reviewer,
      perm_admin
    ])
    db.session.bulk_save_objects(review_status_kinds)
    db.session.commit()

if __name__ == '__main__':
  main()
