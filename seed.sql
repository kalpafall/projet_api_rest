-- USERS
INSERT INTO users (username, email, password_hash, is_active)
VALUES 
  ('admin', 'admin@example.com', 'hashed_admin_pw', true),
  ('mariama', 'mariama@example.com', 'hashed_mariama_pw', true),
  ('guest', 'guest@example.com', 'hashed_guest_pw', false);

-- GROUPS
INSERT INTO groups (name)
VALUES 
  ('admin'),
  ('editor'),
  ('viewer');

-- PROMPTS
INSERT INTO prompts (title, content, created_by)
VALUES 
  ('Bienvenue', 'Ceci est le premier prompt.', 1),
  ('Second test', 'Contenu de test pour prompt 2.', 2);

-- USER_GROUP (liens entre users et groups)
INSERT INTO user_group (user_id, group_id)
VALUES 
  (1, 1), -- admin in admin
  (2, 2), -- mariama in editor
  (3, 3); -- guest in viewer
