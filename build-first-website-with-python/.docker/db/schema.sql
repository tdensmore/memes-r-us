CREATE TABLE `memes` (
  `id` int NOT NULL,
  `url` varchar(255) NOT NULL,
  `creation_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);