-- create table t_account (
--     username varchar(20) not null,
--     person_name varchar(20) not null,
--     surname varchar(20) not null,
--     user_password varchar(60) not null,
--     primary key(username)
-- );

-- create table t_expence (
--     id bigserial primary key,
--     username varchar(20) not null references t_account (username), 
--     category varchar(20) null,
--     exp_description varchar(500) null,
--     exp_amount numeric(15,2) not null,
--     exp_date date not null
-- );

-- create EXTENSION if not exists pgcrypto;

-- create or replace function hash_password()
-- returns TRIGGER as $$
-- begin
--     NEW.user_password := crypt(NEW.user_password, gen_salt('bf'));
--     return NEW;
-- end;
-- $$ language plpgsql;

-- create trigger password_hashing
-- before insert or update OF user_password
-- on t_account
-- for each row
-- execute function hash_password();

