select Name, Location, specialties.Specialty as Specialty 
from docs
join specialties on docs.specialty_id = specialties.id
where name = Bob