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
-- Table structure for table `activities_activityscore`
--

DROP TABLE IF EXISTS `activities_activityscore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities_activityscore` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(40) NOT NULL,
  `score` int NOT NULL,
  `activity_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `activities_activitys_activity_id_id_86daffa3_fk_activitie` (`activity_id_id`),
  CONSTRAINT `activities_activitys_activity_id_id_86daffa3_fk_activitie` FOREIGN KEY (`activity_id_id`) REFERENCES `activities_activity` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities_activityscore`
--

LOCK TABLES `activities_activityscore` WRITE;
/*!40000 ALTER TABLE `activities_activityscore` DISABLE KEYS */;
INSERT INTO `activities_activityscore` VALUES (1,'social',6,1),(2,'physical',6,1),(3,'money',4,1),(4,'social',6,2),(5,'physical',8,2),(6,'money',6,2),(7,'social',4,3),(8,'physical',6,3),(9,'money',2,3),(10,'social',4,4),(11,'physical',4,4),(12,'money',2,4),(13,'social',4,5),(14,'physical',4,5),(15,'money',2,5),(16,'social',4,6),(17,'physical',4,6),(18,'money',2,6),(19,'social',6,7),(20,'physical',6,7),(21,'money',4,7),(22,'social',6,8),(23,'physical',4,8),(24,'money',2,8),(25,'social',2,9),(26,'physical',4,9),(27,'money',2,9),(28,'social',4,10),(29,'physical',4,10),(30,'money',2,10),(31,'social',4,11),(32,'physical',4,11),(33,'money',2,11),(34,'social',4,12),(35,'physical',2,12),(36,'money',2,12),(37,'social',4,13),(38,'physical',2,13),(39,'money',2,13),(40,'social',8,14),(41,'physical',4,14),(42,'money',6,14),(43,'social',4,15),(44,'physical',4,15),(45,'money',2,15),(46,'social',8,16),(47,'physical',4,16),(48,'money',8,16),(49,'social',8,17),(50,'physical',4,17),(51,'money',8,17),(52,'social',8,18),(53,'physical',4,18),(54,'money',8,18),(55,'social',10,19),(56,'physical',8,19),(57,'money',10,19),(58,'social',2,20),(59,'physical',4,20),(60,'money',4,20),(61,'social',2,21),(62,'physical',4,21),(63,'money',4,21),(64,'social',2,22),(65,'physical',4,22),(66,'money',4,22),(67,'social',2,23),(68,'physical',2,23),(69,'money',2,23),(70,'social',2,24),(71,'physical',2,24),(72,'money',2,24),(73,'social',2,25),(74,'physical',2,25),(75,'money',4,25),(76,'social',2,26),(77,'physical',2,26),(78,'money',2,26),(79,'social',2,27),(80,'physical',2,27),(81,'money',2,27),(82,'social',2,28),(83,'physical',2,28),(84,'money',4,28),(85,'social',2,29),(86,'physical',4,29),(87,'money',2,29),(88,'social',2,30),(89,'physical',2,30),(90,'money',2,30);
/*!40000 ALTER TABLE `activities_activityscore` ENABLE KEYS */;
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
