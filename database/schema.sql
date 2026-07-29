-- ==========================================================
-- PETHEALTH - SCRIPT SQL COMPLETO PARA SUPABASE / POSTGRESQL
-- ==========================================================

-- 1. CREACIÓN DE TIPOS ENUM
CREATE TYPE user_role AS ENUM ('free', 'premium', 'admin');
CREATE TYPE pet_species AS ENUM ('dog', 'cat', 'bird', 'rabbit', 'other');
CREATE TYPE record_category AS ENUM ('vaccine', 'deworming', 'consultation', 'surgery', 'lab_result');
CREATE TYPE reminder_interval AS ENUM ('none', 'daily', 'weekly', 'monthly', 'yearly');

-- 2. TABLA USERS
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    role user_role DEFAULT 'free',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_users_email ON users(email);

-- 3. TABLA PETS
CREATE TABLE pets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    species pet_species NOT NULL,
    breed VARCHAR(100),
    birth_date DATE,
    weight_kg DECIMAL(5,2),
    microchip_number VARCHAR(50),
    photo_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_pets_user_id ON pets(user_id);

-- 4. TABLA MEDICAL_RECORDS
CREATE TABLE medical_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pet_id UUID REFERENCES pets(id) ON DELETE CASCADE,
    category record_category NOT NULL,
    title VARCHAR(200) NOT NULL,
    record_date DATE NOT NULL,
    notes TEXT,
    document_image_url TEXT,
    ai_raw_json JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_medical_records_pet_id ON medical_records(pet_id);
CREATE INDEX idx_medical_records_date ON medical_records(record_date DESC);

-- 5. TABLA REMINDERS
CREATE TABLE reminders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pet_id UUID REFERENCES pets(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    due_date TIMESTAMP WITH TIME ZONE NOT NULL,
    repeat_interval reminder_interval DEFAULT 'none',
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_reminders_due_date ON reminders(due_date);