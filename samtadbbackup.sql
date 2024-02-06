-- MariaDB dump 10.19  Distrib 10.4.18-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: samta
-- ------------------------------------------------------
-- Server version	10.4.18-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `grade` float DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (3,'Alice','Smith',18,97),(4,'Jitendra','Kumar',23,95.5),(5,'Vishal','Sharma',24,95.5),(6,'Subhash','Sahani',25,95.5),(7,'Alice','Smith',18,97),(8,'Jitendra','Kumar',23,95.5),(9,'Vishal','Sharma',24,95.5),(10,'Subhash','Sahani',25,95.5),(11,'Avaneesh','Chauhan',27,97),(12,'Aman','Kumar',20,95.5),(13,'Alice','Smith',18,97),(14,'Jitendra','Kumar',23,95.5),(15,'Vishal','Sharma',24,95.5),(16,'Subhash','Sahani',25,95.5),(17,'Avaneesh','Chauhan',27,97),(18,'Aman','Kumar',20,95.5),(19,'Alice','Smith',18,97),(20,'Jitendra','Kumar',23,95.5),(21,'Vishal','Sharma',24,95.5),(22,'Subhash','Sahani',25,95.5),(23,'Avaneesh','Chauhan',27,97),(24,'Aman','Kumar',20,95.5),(25,'Alice','Smith',18,97),(26,'Jitendra','Kumar',23,95.5),(27,'Vishal','Sharma',24,95.5),(28,'Subhash','Sahani',25,95.5),(29,'Avaneesh','Chauhan',27,97),(30,'Aman','Kumar',20,95.5),(31,'Alice','Smith',18,95.5),(32,'Jitendra','Kumar',23,95.5),(33,'Vishal','Sharma',24,95.5),(34,'Subhash','Sahani',25,95.5),(35,'Avaneesh','Chauhan',27,97),(36,'Aman','Kumar',20,95.5);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-06  9:24:37
