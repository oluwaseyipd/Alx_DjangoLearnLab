# Permissions & Groups Setup

- Book model includes custom permissions: can_view, can_create, can_edit, can_delete.
- Groups:
  - Viewers → can_view
  - Editors → can_view, can_create, can_edit
  - Admins → all permissions
- Views use @permission_required decorators to restrict access.
- Assign users to groups via Django admin.
