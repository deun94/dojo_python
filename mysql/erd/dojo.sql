SELECT * FROM owners
JOIN pets on owners.id = pets.owner_id;

SELECT * FROM owners
LEFT JOIN pets on owners.id = pets.owner_id;