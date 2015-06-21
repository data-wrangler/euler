drop table primes;
create table primes (
	id bigserial
	, prime bigint
	, created_at timestamp not null default current_timestamp
	);
create index primes_prime on primes(prime);


create or replace function primes_dedupe() returns trigger as $proc$
	begin
		if exists (
			select 1
			from primes p
			where p.prime= NEW.prime
			)
		then return null;
		end if;
		return NEW;
	end;
$proc$ language plpgsql;

create trigger primes_deduper
	before insert on primes
	for each row execute procedure primes_dedupe();
