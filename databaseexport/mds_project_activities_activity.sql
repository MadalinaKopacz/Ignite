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
-- Table structure for table `activities_activity`
--

DROP TABLE IF EXISTS `activities_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activities_activity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `location` varchar(40) NOT NULL,
  `location_type` varchar(30) NOT NULL,
  `lat` decimal(10,5) NOT NULL,
  `lon` decimal(10,5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities_activity`
--

LOCK TABLES `activities_activity` WRITE;
/*!40000 ALTER TABLE `activities_activity` DISABLE KEYS */;
INSERT INTO `activities_activity` VALUES (1,'going to Cișmigiu Gardens today?','This tree-filled English-style park with a lake, rose garden & pavilion is a tranquil destination.','Cișmigiu Gardens','outdoor',44.43730,26.09110),(2,'going to Herăstrău Park today?','Public green space with cafes, restaurants & gardens around a large lake used for water sports.','Herăstrau Park','outdoor',44.47020,26.08280),(3,'going to Tineretului Park today?','Big park known for its lake, Sala Polivalenta sports complex, kids\' area & trails for cycling.','Tineretului Park','outdoor',44.40790,26.10510),(4,'going to Carol I Park today?','Scenic park established in 1906 featuring a French garden, historical monuments, a mausoleum & lake.','Carol I Park','outdoor',44.41522,26.09592),(5,'going to Kiseleff Park today?','Green space demarcated around 1832, with sculptures & busts of notable Romanians & Roman poet Ovid.','Kiseleff Park','outdoor',44.45770,26.08370),(6,'going to Eroilor Park today?','Would you like to relax alone or with some of your friends? Then the Eroilor Park is ideal for you!','Eroilor Park','outdoor',45.64520,25.59610),(7,'going to Drumul Taberei Park today?','Large urban green space with a lake & a pool, plus a botanical garden, skate park & running trails.','Drumul Taberei Park','outdoor',44.42010,26.03220),(8,'going to Titanii Park today?','Leafy landscaped urban park with water features, fountains & colorful children\'s play equipment.','Titanii Park','outdoor',44.42050,26.16740),(9,'going to Văcăresti Park today?','Protected lakeland with walking paths, plus hides for spotting marsh harriers, moorhens & coots.','Văcărești Park','outdoor',44.39940,26.13320),(10,'going to IOANID Park today?','Intimate urban park since 1870 with statues, benches, a lake & fountain, plus a playground & gazebo.','IOANID Park','outdoor',44.44560,26.10470),(11,'going to Alexandru Ioan Cuza Park today?','Large park featuring a lake with 5 small islands, plus a church, playgrounds & sports facilities.','Alexandru Ioan Cuza Park','outdoor',44.42550,26.15350),(12,'going to Bordei Park today?','Small park with walking paths along a serpentine lake with wetlands & a bridge to a small island.','Bordei Park','outdoor',44.47260,26.09110),(13,'going to  Izvor Park today?','Urban green space opposite the Palace of Parliament featuring open lawn areas & a playground.','Izvor Park','outdoor',44.47260,26.08750),(14,'going to Children\'s World Park today?','Playgrounds, BBQ pits & flower-lined paths in a tranquil recreation area of a busy amusement park.','Children\'s World Park','outdoor',44.40460,26.11520),(15,'going to Morarilor Park today?','Suburban gardens with a lake lined by willow trees, plus a dog park, mini-soccer court & play areas.','Morarilor Park','outdoor',44.43943,26.17071),(16,'going to Nomad Skybar?','Trendy rooftop venue with a glass roof featuring global fare, sharing plates & cocktails, plus DJs.','Nomad Skybar','outdoor',44.43043,26.10008),(17,'going to Caru\' cu bere?','Architecturally notable Romanian restaurant with wood paneling, stained-glass windows & a patio.','Caru\' cu bere?','outdoor',44.43201,26.09812),(18,'going to Bazaar Restaurant?','Laid-back, bi-level eatery offering local fare alongside steaks, burgers, beers & cocktails.','Bazaar Restaurant','outdoor',44.43055,26.10205),(19,'going to the Old Town?','Bucharest’s Old Town is an open-air museum of excavated medieval ruins! It has museums, churches and shops. Elegant restaurants serve traditional dishes and buzzing pubs draw crowds after dark!','Old Town','outdoor',44.42882,26.10989),(20,'going to Romanian National Museum of Art?','The National Museum of Art of Romania is located in the Royal Palace in Revolution Square, central Bucharest. It features collections of medieval and modern Romanian and international art.','Romanian National Museum of Art','outdoor',44.43936,26.09587),(21,'going to National Museum of Romanian History?','The National Museum of Romanian History is a museum located on the Calea Victoriei in Bucharest, Romania, which contains Romanian historical artifacts from prehistoric times up to modern times.','National Museum of Romanian History','outdoor',44.43151,26.09724),(22,'going to The Grigore Antipa National Museum?','The Grigore Antipa National Museum of Natural History is a natural history museum, located in Bucharest, Romania.','The Grigore Antipa National Museum','outdoor',44.45311,26.08463),(23,'reading a book?','Choose a book from your library, try reading a few pages and discover an entire new universe or new stuff about your passions!','at home','any',0.00000,0.00000),(24,'listening to music?','Open your favorite music app, listen to your favorite playlist and relax!','at home','any',0.00000,0.00000),(25,'cooking?','Try cooking something: your favorite dish or a new recipe found on internet! Have fun being a gastronomic expert and don\'t forget to clean the kitchen afterwards!','at home','indoor',0.00000,0.00000),(26,'watching a movie?','Is there a movie you\'ve been wanting to watch for a long time? Bring some popcorn or a snack and enjoy it!','at home','indoor',0.00000,0.00000),(27,'watching a documentary?','What passions do you have? Choose one and search online for a documentary about it!','at home','indoor',0.00000,0.00000),(28,'researching your interests?','What are your hobbies and interests? Choose a few and search for new info about them!','at home','indoor',0.00000,0.00000),(29,'cleaning up your room?','If needed, you can clean your room! This way, you can organize your thoughts and get rid of clutter!','at home','indoor',0.00000,0.00000),(30,'stargazing?','Go outside or sit by the window and admire the stars, the moon and live in the present!','at home','any',0.00000,0.00000);
/*!40000 ALTER TABLE `activities_activity` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-13 12:54:13
