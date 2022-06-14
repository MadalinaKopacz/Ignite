-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: mds_project
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `lat` decimal(10,5) NOT NULL,
  `lon` decimal(10,5) NOT NULL,
  `streaks` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$320000$tZNFL6xgSDgMZrO3tGuPv3$xfYGftxSynWhOYIunMNi87wzKT/CO055vU26f1jqSms=','2022-06-12 17:29:43.852797',0,'mentolnothingmore','Maria-Daniela','Negrut','dani@mail.com',0,1,'2022-06-12 17:12:49.707324','uploads/dani.jpeg',44.44179,26.01357,0),(2,'pbkdf2_sha256$320000$J4Y20RXR4e9uscIJJwCWck$LZCjh+BU90mBKxrCAXeeKs7+yWVq6TRW6lK7/HDLXUU=',NULL,0,'mateidorian','Matei-Dorian','Nastase','matei@mail.com',0,1,'2022-06-12 17:15:33.146369','uploads/matei.jpeg',44.44141,26.01669,0),(3,'pbkdf2_sha256$320000$o75q2YeTWew8lFWRx7eqPN$GpgSmtatuiVbgIXd5RNYVjNKuAAtxWbhnX7pzufVHMA=','2022-06-12 17:26:55.359400',0,'madak','Madalina-Elena','Kopacz','mada@mail.com',0,1,'2022-06-12 17:16:44.095915','uploads/mada.jpeg',44.44258,26.01459,0),(4,'pbkdf2_sha256$320000$MGncknmVGH3peUnjowGbap$Xe0G+js1yqZ4KFFgWoiix+4UGIOT6jbsu/HssVJ/WJA=',NULL,0,'vlad','Vlad-Andrei','Ionescu','vlad@email.com',0,1,'2022-06-12 17:41:24.607693','uploads/vlad.jpeg',44.44191,26.01847,0);
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-14 14:52:34
