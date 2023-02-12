
-- CREATE TABLE `pk` (
--   `id` int(11) NOT NULL,
--   `name` varchar(45) DEFAULT NULL,
--   `imagen` varchar(45) DEFAULT NULL,
--   `abilities` varchar(45) DEFAULT NULL,
--   `stat` varchar(45) DEFAULT NULL,
--   `type` varchar(45) DEFAULT NULL,
--   PRIMARY KEY (`id`),
--   UNIQUE KEY `id_UNIQUE` (`id`)
-- ) 

CREATE TABLE pokemons (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  image_url VARCHAR(255) NOT NULL
);

CREATE TABLE pokemon_stats (
  id INT PRIMARY KEY AUTO_INCREMENT,
  pokemon_id INT NOT NULL,
  stat VARCHAR(255) NOT NULL,
  base_stat INT NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);

CREATE TABLE pokemon_abilities (
  id INT PRIMARY KEY AUTO_INCREMENT,
  pokemon_id INT NOT NULL,
  ability VARCHAR(255) NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);

CREATE TABLE pokemon_types (
  id INT PRIMARY KEY AUTO_INCREMENT,
  pokemon_id INT NOT NULL,
  type VARCHAR(255) NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES pokemons(id)
);
