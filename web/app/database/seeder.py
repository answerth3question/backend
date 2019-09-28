from app.database.db import db
from app.database.models import UserRole, UserPermission, ReviewStatusKind

def seed_db():
  role_contributer = UserRole(name='contributer')
  role_reviewer = UserRole(name='reviewer')
  role_admin = UserRole(name='admin')

  db.session.add_all([
    role_contributer,
    role_reviewer,
    role_admin,
  ])
 
  perm_contributer = UserPermission(name='contributer')
  perm_reviewer = UserPermission(name='reviewer')
  perm_admin = UserPermission(name='admin')

  role_contributer.permission.append(perm_contributer)

  role_reviewer.permission.append(perm_contributer)
  role_reviewer.permission.append(perm_reviewer)

  role_admin.permission.append(perm_contributer)
  role_admin.permission.append(perm_reviewer)
  role_admin.permission.append(perm_admin)

  db.session.add_all([
    perm_contributer,
    perm_reviewer,
    perm_admin
  ])

  db.session.add_all([
    ReviewStatusKind(name='pending'),
    ReviewStatusKind(name='rejected'),
    ReviewStatusKind(name='approved'),
  ])

  db.session.commit()
