-- MyGTS Database Schema (Supabase / PostgreSQL)
-- Dibuat oleh: Orang 3 (Model Layer)
-- Jalankan script ini di Supabase SQL Editor

-- Tabel users
CREATE TABLE IF NOT EXISTS users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL,
    email       TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role        TEXT NOT NULL CHECK (role IN ('customer', 'owner')),
    phone       TEXT DEFAULT '',
    created_at  TIMESTAMPTZ DEFAULT now()
);

-- Tabel inventories
CREATE TABLE IF NOT EXISTS inventories (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name          TEXT NOT NULL,
    category      TEXT NOT NULL,
    description   TEXT DEFAULT '',
    stock         INTEGER NOT NULL DEFAULT 0,
    price_per_day INTEGER NOT NULL DEFAULT 0,
    condition     TEXT DEFAULT 'Baik',
    image_url     TEXT DEFAULT '',
    created_at    TIMESTAMPTZ DEFAULT now()
);

-- Tabel rentals
CREATE TABLE IF NOT EXISTS rentals (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id           UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    inventory_id      UUID NOT NULL REFERENCES inventories(id) ON DELETE CASCADE,
    start_date        DATE NOT NULL,
    end_date          DATE NOT NULL,
    return_date       DATE,
    status            TEXT NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending', 'confirmed', 'active', 'returned', 'rejected')),
    pickup_photo_url  TEXT DEFAULT '',
    return_photo_url  TEXT DEFAULT '',
    fine_amount       INTEGER DEFAULT 0,
    notes             TEXT DEFAULT '',
    created_at        TIMESTAMPTZ DEFAULT now()
);

-- Index untuk performa query umum
CREATE INDEX IF NOT EXISTS idx_rentals_user    ON rentals(user_id);
CREATE INDEX IF NOT EXISTS idx_rentals_status  ON rentals(status);
CREATE INDEX IF NOT EXISTS idx_inv_category    ON inventories(category);

-- Seed: akun owner default (password: owner123)
INSERT INTO users (name, email, password_hash, role)
VALUES (
    'Admin Sanggar',
    'owner@mygts.com',
    'ef92b778bafe771207ca7d27cef2c0e7f83cdad2f2ecca90e4effd9eff2eba1f', -- sha256('owner123')
    'owner'
) ON CONFLICT DO NOTHING;
