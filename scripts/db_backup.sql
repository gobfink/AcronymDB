USE acronym;
-- MySQL dump 10.13  Distrib 8.0.17, for Linux (x86_64)
--
-- Host: db    Database: acronym
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_AcroTag`
--

DROP TABLE IF EXISTS `tbl_AcroTag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_AcroTag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `acroID` bigint(20) NOT NULL,
  `tagID` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_AcroTag`
--

LOCK TABLES `tbl_AcroTag` WRITE;
/*!40000 ALTER TABLE `tbl_AcroTag` DISABLE KEYS */;
INSERT INTO `tbl_AcroTag` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `tbl_AcroTag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_Acronym`
--

DROP TABLE IF EXISTS `tbl_Acronym`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_Acronym` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `acronym` varchar(80) NOT NULL,
  `definition` varchar(80) NOT NULL,
  `author_id` bigint(20) DEFAULT NULL,
  `dateCreate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_Acronym`
--

LOCK TABLES `tbl_Acronym` WRITE;
/*!40000 ALTER TABLE `tbl_Acronym` DISABLE KEYS */;
INSERT INTO `tbl_Acronym` VALUES (1,'TBD','To Be Determined',1,'2019-09-20 01:24:28'),(2,'ASAP','As Soon As Possible',1,'2019-09-20 01:24:28'),(8,'New Acro','This is atest Acronym',1,'2019-10-01 16:49:00');
/*!40000 ALTER TABLE `tbl_Acronym` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_Tag`
--

DROP TABLE IF EXISTS `tbl_Tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_Tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Tag` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `acroID` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_Tag`
--

LOCK TABLES `tbl_Tag` WRITE;
/*!40000 ALTER TABLE `tbl_Tag` DISABLE KEYS */;
INSERT INTO `tbl_Tag` VALUES (1,'US Navy'),(2,'ASSETT'),(3,'General'),(4,'Test 4');
/*!40000 ALTER TABLE `tbl_Tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_User`
--

DROP TABLE IF EXISTS `tbl_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_User` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(80) NOT NULL,
  `username` varchar(80) NOT NULL,
  `userFN` varchar(80) DEFAULT NULL,
  `userLN` varchar(80) DEFAULT NULL,
  `userPasswordHash` varchar(128) DEFAULT NULL,
  `userIsAdmin` int(11) DEFAULT NULL,
  `userLastLoginDT` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_User`
--

LOCK TABLES `tbl_User` WRITE;
/*!40000 ALTER TABLE `tbl_User` DISABLE KEYS */;
INSERT INTO `tbl_User` VALUES (1,'kgustafson2@gmail.com','kgustafson','Kurt','Gustafson','pbkdf2:sha256:150000$QdXtO1tr$f3cbce0096438589d64d074f40b7aeef84f6e327b3275a13077046e9fb5da786',1,'2019-09-13 19:20:49'),(2,'alex.kayser@assett.net','akayser','Alex','Kayser','pbkdf2:sha256:150000$CXYV7eBs$fa7bafbc3dd2d6c93346a255b39731877a7bd3cbfa51ccd0da3dbc8860237585',1,'2019-09-18 16:11:29'),(3,'gobfink@gmail.com','afortman','Andy','Fortman','pbkdf2:sha256:150000$TMqBdxVa$cbda14148a321f7f4666c873bccbbdcfc25907d21e2e9ee337dafc446fbb2ba7',1,'2019-09-18 16:29:11'),(4,'jim.viar@assett.net','jim','jim','viar','pbkdf2:sha256:150000$XWbQpUiX$f9875f604a3a16ec94eae5259c35e9d1778dbb1c749dc032411062511d94cd34',1,'2019-10-09 20:59:22');
/*!40000 ALTER TABLE `tbl_User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-09 21:01:36
