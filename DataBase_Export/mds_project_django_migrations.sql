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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-06-12 16:39:48.078411'),(2,'contenttypes','0002_remove_content_type_name','2022-06-12 16:39:48.123288'),(3,'auth','0001_initial','2022-06-12 16:39:48.336117'),(4,'auth','0002_alter_permission_name_max_length','2022-06-12 16:39:48.376195'),(5,'auth','0003_alter_user_email_max_length','2022-06-12 16:39:48.384014'),(6,'auth','0004_alter_user_username_opts','2022-06-12 16:39:48.393553'),(7,'auth','0005_alter_user_last_login_null','2022-06-12 16:39:48.413873'),(8,'auth','0006_require_contenttypes_0002','2022-06-12 16:39:48.421179'),(9,'auth','0007_alter_validators_add_error_messages','2022-06-12 16:39:48.433932'),(10,'auth','0008_alter_user_username_max_length','2022-06-12 16:39:48.444207'),(11,'auth','0009_alter_user_last_name_max_length','2022-06-12 16:39:48.453288'),(12,'auth','0010_alter_group_name_max_length','2022-06-12 16:39:48.468458'),(13,'auth','0011_update_proxy_permissions','2022-06-12 16:39:48.478186'),(14,'auth','0012_alter_user_first_name_max_length','2022-06-12 16:39:48.487132'),(15,'accounts','0001_initial','2022-06-12 16:39:49.000100'),(16,'accounts','0002_user_lat_user_lon','2022-06-12 16:39:49.165973'),(17,'activities','0001_initial','2022-06-12 16:39:49.295584'),(18,'activities','0002_activity_lat_activity_lon','2022-06-12 16:39:49.359495'),(19,'admin','0001_initial','2022-06-12 16:39:49.479648'),(20,'admin','0002_logentry_remove_auto_add','2022-06-12 16:39:49.493928'),(21,'admin','0003_logentry_add_action_flag_choices','2022-06-12 16:39:49.506687'),(22,'mood_quizzes','0001_initial','2022-06-12 16:39:49.528785'),(23,'sessions','0001_initial','2022-06-12 16:39:49.569879'),(24,'activities','0003_alter_activity_location_type','2022-06-13 07:44:21.901126'),(25,'accounts','0003_user_streaks','2022-06-13 16:56:50.869878');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
