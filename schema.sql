-- Table: users
create table if not exists users (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  supabase_user_id text not null unique,
  created_at timestamp default now()
);

-- Table: parsed_lessons
create table if not exists parsed_lessons (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id),
  unit_title text,
  content jsonb,
  created_at timestamp default now()
);

-- Table: ai_suggestions
create table if not exists ai_suggestions (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid references parsed_lessons(id),
  type text, -- 'objective' | 'scaffold' | 'protocol' | 'assessment'
  suggestion text,
  metadata jsonb,
  created_at timestamp default now()
);

-- Table: feedback
create table if not exists feedback (
  id uuid primary key default gen_random_uuid(),
  suggestion_id uuid references ai_suggestions(id),
  feedback_type text, -- 'accept' | 'edit' | 'reject'
  comments text,
  created_at timestamp default now()
);

-- Table: lesson_embeddings
create table if not exists lesson_embeddings (
  id uuid primary key default gen_random_uuid(),
  lesson_id uuid references parsed_lessons(id),
  content text,
  embedding vector(1536) -- assuming OpenAI embeddings
);
