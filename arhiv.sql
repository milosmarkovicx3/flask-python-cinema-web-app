-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2023 at 09:44 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `arhiv`
--

-- --------------------------------------------------------

--
-- Table structure for table `actor`
--

CREATE TABLE `actor` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `actor`
--

INSERT INTO `actor` (`id`, `name`, `image`) VALUES
(1, 'Luke Evans', 'luke_evans.jpg'),
(2, 'Sarah Gadon', 'sarah_gadon.png'),
(3, 'Dominic Cooper', 'dominic_cooper.png'),
(4, 'Charles Dance', 'charles_dance.png'),
(5, 'Meryl Streep', 'meryl_streep.png'),
(6, 'Robert De Niro', 'robert_de_niro.png'),
(7, 'John Cazale', 'john_cazale.jpg'),
(8, 'Christopher Walken', 'christopher_walken.png'),
(9, 'Tom Hardy', 'tom_hardy.jpg'),
(10, 'Philip Seymour Hoffman', 'philip_seymour_hoffman.jpg'),
(11, 'Josef Altin', 'josef_altin.png'),
(12, 'Fares Fares', 'fares_fares.jpg'),
(13, 'Jason Clarke', 'jason_clarke.jpg'),
(14, 'Xavier Atkins', 'xavier_atkins.jpg'),
(15, 'Gary Oldman', 'gary_oldman.jpg'),
(16, 'Noomi Rapace', 'noomi_rapace.jpg'),
(17, 'Joel Kinnaman', 'joel_kinnaman.png'),
(18, 'Vincent Cassel', 'vincent_cassel.png'),
(19, 'Paddy Considine', 'paddy_considine.jpg'),
(20, 'Stephen Graham', 'stephen_graham.png'),
(21, 'Stephen Lang', 'stephen_lang.png'),
(22, 'David Wenham', 'david_wenham.png'),
(23, 'Billy Crudup', 'billy_crudup.png'),
(24, 'Carey Mulligan', 'carey_mulligan.png'),
(25, 'Giovanni Ribisi', 'giovanni_ribisi.png'),
(26, 'Leelee Sobieski', 'leelee_sobieski.jpg'),
(27, 'Marion Cotillard', 'marion_cotillard.jpg'),
(28, 'Christian Bale', 'christian_bale.jpg'),
(29, 'Channing Tatum', 'channing_tatum.png'),
(30, 'Johnny Depp', 'johnny_depp.jpg'),
(31, 'Bryan Callen', 'bryan_callen.jpg'),
(32, 'Maximiliano Hernandez', 'maximiliano_hernández.png'),
(33, 'Kevin Dunn', 'kevin_dunn.jpg'),
(34, 'Jennifer Morrison', 'jennifer_morrison.jpg'),
(35, 'Frank Grillo', 'frank_grillo.png'),
(36, 'Joel Edgerton', 'joel_edgerton.jpg'),
(37, 'Nick Nolte', 'nick_nolte.jpg'),
(38, 'Chris Hemsworth', 'chris_hemsworth.png'),
(39, 'Keanu Reeves', 'keanu_reeves.jpg'),
(40, 'Laurence Fishburne', 'laurence_fishburne.jpg'),
(41, 'Carrie-Anne Moss', 'carrie_anne_moss.png'),
(42, 'Hugo Weaving', 'hugo_weaving.png'),
(43, 'Ben Affleck', 'ben_affleck.jpg'),
(44, 'Matt Damon', 'matt_damon.jpg'),
(45, 'Robin Williams', 'robin_williams.png'),
(46, 'Stellan Skarsgard', 'stellan_skarsgard.png'),
(47, 'Rachel Majorowski', 'rachel_majorowski.png'),
(48, 'Casey Affleck', 'casey_affleck.png'),
(49, 'Ethan Hawke', 'ethan_awke.png'),
(50, 'Uma Thurman', 'uma_thurman.png'),
(51, 'Jude Law', 'jude_law.png'),
(52, 'Brad Pitt', 'brad_pitt.png'),
(53, 'Anthony Hopkins', 'anthony_hopkins.png'),
(54, 'Aidan Quinn', 'aidan_quinn.png'),
(55, 'Julia Ormond', 'julia_ormond.png'),
(56, 'Michael Madsen', 'michael_madsen.png'),
(57, 'Al Pacino', 'al_pacino.png'),
(58, 'Bruno Kirby', 'bruno_kirby.png'),
(59, 'James Russo', 'james_russo.png'),
(60, 'Harrison Ford', 'harrison_ford.jpg'),
(61, 'Rutger Hauer', 'rutger_hauer.jpg'),
(62, 'Sean Young', 'sean_young.png'),
(63, 'Michael Fassbender', 'michael_fassbender.jpg'),
(64, 'Karen Hassan', 'karen_hassan.jpg'),
(65, 'Brian Milligan', 'brian_milligan.png'),
(66, 'Liam McMahon', 'liam_mcmahon.png'),
(67, 'Stuart Graham', 'stuart_graham.jpg'),
(68, 'Ed Harris', 'ed_harris.jpg'),
(69, 'Joseph Fiennes', 'joseph_fiennes.jpg'),
(70, 'Rachel Weisz', 'rachel_weisz.jpg'),
(71, 'Bob Hoskins', 'bob_hoskins.jpg'),
(72, 'Ron Perlman', 'ron_perlman.png');

-- --------------------------------------------------------

--
-- Table structure for table `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `genre`
--

INSERT INTO `genre` (`id`, `name`, `image`) VALUES
(1, 'Action', 'action.png'),
(2, 'Adventure', 'adventure.png'),
(3, 'Drama', 'drama.png'),
(4, 'Fantasy', 'fantasy.png'),
(5, 'War', 'war.png'),
(6, 'History', 'history.png'),
(7, 'Crime', 'crime.png'),
(8, 'Biography ', 'biography.png'),
(9, 'Sport', 'sport.jpeg'),
(10, 'Animation', 'animation.jpg'),
(11, 'Science Fiction', 'science_fiction.png'),
(12, 'Romance', 'romance.png'),
(13, 'Thriller ', 'thriller.png');

-- --------------------------------------------------------

--
-- Table structure for table `hall`
--

CREATE TABLE `hall` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `capacity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hall`
--

INSERT INTO `hall` (`id`, `name`, `capacity`) VALUES
(1, 'Marilyn Monroe', 76),
(2, 'James Dean', 60);

-- --------------------------------------------------------

--
-- Table structure for table `mailing_list`
--

CREATE TABLE `mailing_list` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `movie`
--

CREATE TABLE `movie` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `year` int(11) NOT NULL,
  `duration` varchar(255) NOT NULL,
  `rating` varchar(255) NOT NULL,
  `votes` int(11) NOT NULL,
  `poster` varchar(255) NOT NULL,
  `trailer` varchar(1024) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movie`
--

INSERT INTO `movie` (`id`, `title`, `year`, `duration`, `rating`, `votes`, `poster`, `trailer`) VALUES
(1, 'Dracula Untold', 2014, '1h 32m', '6.2', 201000, 'dracula_untold.png', 'https://drive.google.com/file/d/1rjPvSm8av6jVMp7-LivbFfU-TW7QBEAO/preview'),
(2, 'The Deer Hunter', 1978, '3h 3m', '8.1', 346000, 'the_deer_hunter.png', 'https://drive.google.com/file/d/1TRmA_JtH5CQwDTP9F-fxuvS24G0nUEcX/preview'),
(3, 'Child 44', 2015, '2h 17m', '6.4', 73000, 'child_44.png', 'https://drive.google.com/file/d/1K8yHfWXU0CBCrl28HBQ7aGu_ggcrU98f/preview'),
(4, 'Public Enemies', 2009, '2h 20m', '7.0', 309000, 'public_enemies.png', 'https://drive.google.com/file/d/1YmtJwjv-w4-clzWgNS8aY797kYXW-Mie/preview'),
(5, 'Warrior', 2011, '2h 20m', '8.2', 481000, 'warrior.png', 'https://drive.google.com/file/d/1AYhhosCDmoqxim4qqhiH3cyEcwl5AUoI/preview'),
(6, 'The Matrix', 1999, '2h 16m', '8.7', 2000000, 'the_matrix.jpg', 'https://drive.google.com/file/d/1iSix9K7WOyCvd9cTRD1Gy2C50f6kCgWW/preview'),
(7, 'Good Will Hunting', 1997, '2h 6m', '8.3', 1000000, 'good_will_hunting.png', 'https://drive.google.com/file/d/1rlqkoAPXcEd-Iwo1fhnQqg7w6SEQYCJu/preview'),
(8, 'Gattaca', 1997, '1h 46m', '7.8', 312000, 'gattaca.png', 'https://drive.google.com/file/d/1Ko0wz52LsOAktF6WQz4o1xDnvUZN3RI1/preview'),
(9, 'Legends of the Fall', 1994, '2h 13m', '7.5', 173000, 'legends_of_the_fall.png', 'https://drive.google.com/file/d/1kqAsYqIZnccs6FEPqJ2VtJtIbxqbXkq4/preview'),
(10, 'Donnie Brasco', 1997, '2h 7m', '7.7', 316000, 'donnie_brasco.png', 'https://drive.google.com/file/d/1zoRJGL2P10CbGIUHCI17aOQpPleXqMvp/preview'),
(11, 'Blade Runner', 1982, '1h 57m', '8.1', 786000, 'blade_runner.jpg', 'https://drive.google.com/file/d/1sTvfm6VONLff1IvDinVQXj4fvzOx4lve/preview'),
(12, 'Hunger', 2008, '1h 36m', '7.5', 72000, 'hunger.jpg', 'https://drive.google.com/file/d/1A7PpTuo6zSDrCLrfB5f-0Lj2K28OfQbI/preview'),
(13, 'Enemy at the Gates', 2001, '2h 11m', '7.5', 268000, 'enemy_at_the_gates.jpg', 'https://drive.google.com/file/d/1n1YjwfmXAlUCGmB0ODDH35OpXeNhOQBL/preview');

-- --------------------------------------------------------

--
-- Table structure for table `movies_genres`
--

CREATE TABLE `movies_genres` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies_genres`
--

INSERT INTO `movies_genres` (`id`, `movie_id`, `genre_id`) VALUES
(1, 1, 1),
(2, 1, 3),
(3, 1, 4),
(4, 2, 3),
(5, 2, 5),
(6, 3, 3),
(7, 3, 6),
(8, 3, 7),
(9, 4, 1),
(10, 4, 7),
(11, 4, 8),
(12, 5, 1),
(13, 5, 3),
(14, 5, 9),
(20, 6, 1),
(21, 6, 11),
(22, 7, 3),
(23, 7, 12),
(24, 8, 13),
(25, 8, 3),
(26, 8, 11),
(27, 9, 3),
(28, 9, 12),
(29, 9, 5),
(30, 10, 8),
(31, 10, 7),
(32, 10, 3),
(33, 11, 1),
(34, 11, 3),
(35, 11, 11),
(36, 12, 8),
(37, 12, 7),
(38, 12, 3),
(39, 13, 1),
(40, 13, 3),
(41, 13, 5);

-- --------------------------------------------------------

--
-- Table structure for table `projection`
--

CREATE TABLE `projection` (
  `id` int(11) NOT NULL,
  `hall_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `projection`
--

INSERT INTO `projection` (`id`, `hall_id`, `movie_id`, `date`, `time`) VALUES
(21, 1, 1, '2023-05-15', '20:00:00'),
(22, 1, 1, '2023-05-16', '20:00:00'),
(23, 1, 1, '2023-05-17', '20:00:00'),
(24, 1, 1, '2023-05-18', '20:00:00'),
(25, 1, 1, '2023-05-19', '20:00:00'),
(26, 1, 1, '2023-05-20', '20:00:00'),
(27, 1, 1, '2023-05-21', '20:00:00'),
(28, 1, 1, '2023-05-22', '20:00:00'),
(29, 1, 1, '2023-05-23', '20:00:00'),
(30, 1, 1, '2023-05-24', '20:00:00'),
(31, 1, 1, '2023-05-25', '20:00:00'),
(32, 1, 1, '2023-05-26', '20:00:00'),
(33, 1, 1, '2023-05-27', '20:00:00'),
(34, 1, 1, '2023-05-28', '20:00:00'),
(35, 1, 1, '2023-05-29', '20:00:00'),
(36, 1, 1, '2023-05-30', '20:00:00'),
(37, 1, 1, '2023-05-31', '20:00:00'),
(38, 1, 1, '2023-06-01', '20:00:00'),
(39, 1, 1, '2023-06-02', '20:00:00'),
(40, 1, 1, '2023-06-03', '20:00:00'),
(41, 1, 1, '2023-06-04', '20:00:00'),
(42, 1, 1, '2023-06-05', '20:00:00'),
(43, 1, 1, '2023-06-06', '20:00:00'),
(44, 1, 1, '2023-06-07', '20:00:00'),
(45, 1, 1, '2023-06-08', '20:00:00'),
(46, 1, 1, '2023-06-09', '20:00:00'),
(47, 1, 1, '2023-06-10', '20:00:00'),
(48, 1, 1, '2023-06-11', '20:00:00'),
(49, 1, 1, '2023-06-12', '20:00:00'),
(50, 1, 1, '2023-06-13', '20:00:00'),
(51, 1, 1, '2023-06-14', '20:00:00'),
(52, 1, 1, '2023-06-15', '20:00:00'),
(53, 1, 1, '2023-06-16', '20:00:00'),
(54, 1, 1, '2023-06-17', '20:00:00'),
(55, 1, 1, '2023-06-18', '20:00:00'),
(56, 1, 1, '2023-06-19', '20:00:00'),
(57, 1, 1, '2023-06-20', '20:00:00'),
(58, 1, 1, '2023-06-21', '20:00:00'),
(59, 1, 1, '2023-06-22', '20:00:00'),
(60, 1, 1, '2023-06-23', '20:00:00'),
(61, 1, 1, '2023-06-24', '20:00:00'),
(62, 1, 1, '2023-06-25', '20:00:00'),
(63, 1, 1, '2023-06-26', '20:00:00'),
(64, 1, 1, '2023-06-27', '20:00:00'),
(65, 1, 1, '2023-06-28', '20:00:00'),
(66, 1, 1, '2023-06-29', '20:00:00'),
(67, 1, 1, '2023-06-30', '20:00:00'),
(68, 1, 1, '2023-07-01', '20:00:00'),
(69, 1, 1, '2023-07-02', '20:00:00'),
(70, 1, 1, '2023-07-03', '20:00:00'),
(71, 1, 1, '2023-07-04', '20:00:00'),
(72, 1, 1, '2023-07-05', '20:00:00'),
(73, 1, 1, '2023-07-06', '20:00:00'),
(74, 1, 1, '2023-07-07', '20:00:00'),
(75, 1, 1, '2023-07-08', '20:00:00'),
(76, 1, 1, '2023-07-09', '20:00:00'),
(77, 1, 1, '2023-07-10', '20:00:00'),
(78, 1, 1, '2023-07-11', '20:00:00'),
(79, 1, 1, '2023-07-12', '20:00:00'),
(80, 1, 1, '2023-07-13', '20:00:00'),
(81, 1, 1, '2023-07-14', '20:00:00'),
(82, 1, 1, '2023-07-15', '20:00:00'),
(83, 1, 1, '2023-07-16', '20:00:00'),
(84, 1, 1, '2023-07-17', '20:00:00'),
(85, 1, 1, '2023-07-18', '20:00:00'),
(86, 1, 1, '2023-07-19', '20:00:00'),
(87, 1, 1, '2023-07-20', '20:00:00'),
(88, 1, 1, '2023-07-21', '20:00:00'),
(89, 1, 1, '2023-07-22', '20:00:00'),
(90, 1, 1, '2023-07-23', '20:00:00'),
(91, 1, 1, '2023-07-24', '20:00:00'),
(92, 1, 1, '2023-07-25', '20:00:00'),
(93, 1, 1, '2023-07-26', '20:00:00'),
(94, 1, 1, '2023-07-27', '20:00:00'),
(95, 1, 1, '2023-07-28', '20:00:00'),
(96, 1, 1, '2023-07-29', '20:00:00'),
(97, 1, 1, '2023-07-30', '20:00:00'),
(103, 2, 1, '2023-05-15', '12:45:00'),
(104, 2, 1, '2023-05-16', '12:45:00'),
(105, 2, 1, '2023-05-17', '12:45:00'),
(106, 2, 1, '2023-05-18', '12:45:00'),
(107, 2, 1, '2023-05-19', '12:45:00'),
(108, 2, 1, '2023-05-20', '12:45:00'),
(109, 2, 1, '2023-05-21', '12:45:00'),
(110, 2, 1, '2023-05-22', '12:45:00'),
(111, 2, 1, '2023-05-23', '12:45:00'),
(112, 2, 1, '2023-05-24', '12:45:00'),
(113, 2, 1, '2023-05-25', '12:45:00'),
(114, 2, 1, '2023-05-26', '12:45:00'),
(115, 2, 1, '2023-05-27', '12:45:00'),
(116, 2, 1, '2023-05-28', '12:45:00'),
(117, 2, 1, '2023-05-29', '12:45:00'),
(118, 2, 1, '2023-05-30', '12:45:00'),
(119, 2, 1, '2023-05-31', '12:45:00'),
(120, 2, 1, '2023-06-01', '12:45:00'),
(121, 2, 1, '2023-06-02', '12:45:00'),
(122, 2, 1, '2023-06-03', '12:45:00'),
(123, 2, 1, '2023-06-04', '12:45:00'),
(124, 2, 1, '2023-06-05', '12:45:00'),
(125, 2, 1, '2023-06-06', '12:45:00'),
(126, 2, 1, '2023-06-07', '12:45:00'),
(127, 2, 1, '2023-06-08', '12:45:00'),
(128, 2, 1, '2023-06-09', '12:45:00'),
(129, 2, 1, '2023-06-10', '12:45:00'),
(130, 2, 1, '2023-06-11', '12:45:00'),
(131, 2, 1, '2023-06-12', '12:45:00'),
(132, 2, 1, '2023-06-13', '12:45:00'),
(133, 2, 1, '2023-06-14', '12:45:00'),
(134, 2, 1, '2023-06-15', '12:45:00'),
(135, 2, 1, '2023-06-16', '12:45:00'),
(136, 2, 1, '2023-06-17', '12:45:00'),
(137, 2, 1, '2023-06-18', '12:45:00'),
(138, 2, 1, '2023-06-19', '12:45:00'),
(139, 2, 1, '2023-06-20', '12:45:00'),
(140, 2, 1, '2023-06-21', '12:45:00'),
(141, 2, 1, '2023-06-22', '12:45:00'),
(142, 2, 1, '2023-06-23', '12:45:00'),
(143, 2, 1, '2023-06-24', '12:45:00'),
(144, 2, 1, '2023-06-25', '12:45:00'),
(145, 2, 1, '2023-06-26', '12:45:00'),
(146, 2, 1, '2023-06-27', '12:45:00'),
(147, 2, 1, '2023-06-28', '12:45:00'),
(148, 2, 1, '2023-06-29', '12:45:00'),
(149, 2, 1, '2023-06-30', '12:45:00'),
(150, 2, 1, '2023-07-01', '12:45:00'),
(151, 2, 1, '2023-07-02', '12:45:00'),
(152, 2, 1, '2023-07-03', '12:45:00'),
(153, 2, 1, '2023-07-04', '12:45:00'),
(154, 2, 1, '2023-07-05', '12:45:00'),
(155, 2, 1, '2023-07-06', '12:45:00'),
(156, 2, 1, '2023-07-07', '12:45:00'),
(157, 2, 1, '2023-07-08', '12:45:00'),
(158, 2, 1, '2023-07-09', '12:45:00'),
(159, 2, 1, '2023-07-10', '12:45:00'),
(160, 2, 1, '2023-07-11', '12:45:00'),
(161, 2, 1, '2023-07-12', '12:45:00'),
(162, 2, 1, '2023-07-13', '12:45:00'),
(163, 2, 1, '2023-07-14', '12:45:00'),
(164, 2, 1, '2023-07-15', '12:45:00'),
(165, 2, 1, '2023-07-16', '12:45:00'),
(166, 2, 1, '2023-07-17', '12:45:00'),
(167, 2, 1, '2023-07-18', '12:45:00'),
(168, 2, 1, '2023-07-19', '12:45:00'),
(169, 2, 1, '2023-07-20', '12:45:00'),
(170, 2, 1, '2023-07-21', '12:45:00'),
(171, 2, 1, '2023-07-22', '12:45:00'),
(172, 2, 1, '2023-07-23', '12:45:00'),
(173, 2, 1, '2023-07-24', '12:45:00'),
(174, 2, 1, '2023-07-25', '12:45:00'),
(175, 2, 1, '2023-07-26', '12:45:00'),
(176, 2, 1, '2023-07-27', '12:45:00'),
(177, 2, 1, '2023-07-28', '12:45:00'),
(178, 2, 1, '2023-07-29', '12:45:00'),
(179, 2, 1, '2023-07-30', '12:45:00');

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `id` int(11) NOT NULL,
  `projection_id` int(11) NOT NULL,
  `seat_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `comment` varchar(2048) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `created_at` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`id`, `user_id`, `movie_id`, `comment`, `rating`, `created_at`) VALUES
(1, 1, 1, 'Film mi se svideo iz razloga što u klasičnim filmovima vampire predstavljaju kao loše karaktere bez ikakvog konteksta vezanog za njihovu prošlost, dok je Vlad u početku prikazan kao običan porodičan čovek koji usled neočekivanih okolnosti biva prinuđen da se bori za svoje najbliže svakim dostupnim sredstvom.', 9, '2023-05-10'),
(3, 2, 1, 'Jaka pričica!', 8, '2023-05-10'),
(4, 1, 2, 'Jako dobar film koji prikazuje scene društva u ratu, drugarstva i širok spektar među-ljudskih odnosa i emocija.', 10, '2023-05-13'),
(5, 1, 3, 'Prikazuju se scene društva u Sovjetskom Savezu, društva kontrolisanog političkom moći, života glavnih likova kako na visokoj tako i na niskoj noti i sve to sa dozom romantike.', 9, '2023-05-13'),
(6, 1, 4, 'Priča je u svojoj osnovi poprilično jednostavna, ali sami karakteri su poprilično zanimljivi, od kojih je većina odglumljena od strane poznatih glumaca. John Dillinger kao karakter je prikazan kao jaka, staložena ličnost, poput koje bi mnogi voleli da budu.', 10, '2023-05-13'),
(7, 1, 5, 'Zanimljiva priča o dvojici braće koji su se rastali kao mali usled porodičnih problema, gde im se roditelji razvode i nakon toga se susreću opet kao starije osobe koje izrazuju želju da učestvuju na istom borilačkom turniru. Priča svih glavnih karaktera ujedno predstavlja i priču o problemima sa kojim se svaki od njih susreće u životu.', 10, '2023-05-13'),
(8, 1, 6, 'Genijalan film ispred svog vremena, sa dosta akcije i zanimljivih karaktera.', 10, '2023-05-13'),
(9, 1, 7, 'Priča o životu ekstremno inteligentnog mladića, rođenog u nižem staležu društva i njegovoj promeni načina razmišljanja ili njegovoj elovuciji kao ljudsko biće bolje rečeno nakon ostvarivanja kontakta sa dobrom osobom koja već ima izgrađen stabilan pogled na svet.', 10, '2023-05-13'),
(10, 1, 8, 'Priča o osobi koja želi da pobegne iz kaveza punog ograničenja u koje ga je društvo stavilo prilikom rođenja, njegovom načinu razmišljanja i putu punom opasnosti.', 10, '2023-05-13'),
(11, 1, 9, 'Priča o mirnim vremenima i trojici braće koji se zaljubljuju u istu devojku, nakon čega izbija rat u kojem su sva trojica prinuđeni da učestvuju zbog jednog ili drugog razloga.', 10, '2023-05-13'),
(12, 1, 10, 'Priča o mladiću u policijskom odredu koji se bavi istraživanjem narkotika, tajnoj misiji, mafiji i realnosti sa kojom se mladić susreće, da sve u životu nije ni samo crno ni samo belo, već neka nijansa sive.', 9, '2023-05-13'),
(13, 1, 11, 'Jedan od retkih filmova, koji prosečna osoba pogleda i shvati da je možda glavni negativac ipak bio u pravu.', 9, '2023-05-13'),
(14, 1, 12, 'Priča o zatvorenicima, društu, politici i surovoj realnosti koja se dešava među nama.', 9, '2023-05-13'),
(15, 1, 13, 'Priča o ratu i jednom mladiću kome se život menja 360 stepeni nakon što spase jednog vojnog oficira u bici, kao i romansi i mržnji koja se stvara tokom nastana iste.', 9, '2023-05-13');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `actor_id` int(11) NOT NULL,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`id`, `movie_id`, `actor_id`, `role`) VALUES
(1, 1, 1, 'Vlad'),
(2, 1, 2, 'Mirena'),
(3, 1, 3, 'Mehmed'),
(4, 1, 4, 'Master Vampire'),
(5, 2, 6, 'Michael'),
(6, 2, 7, 'Stan'),
(7, 2, 8, 'Nick'),
(8, 2, 5, 'Linda'),
(9, 3, 9, 'Leo Demidov'),
(10, 3, 11, 'Alexander'),
(11, 3, 12, 'Alexei Andreyev'),
(12, 3, 13, 'Anatoly Brodsky'),
(13, 3, 15, 'Mikhail Nesterov'),
(14, 3, 16, 'Raisa Demidova'),
(15, 3, 17, 'Vasili Nikitin'),
(16, 3, 18, 'Major Kuzmin'),
(17, 3, 19, 'Vladimir Malevich'),
(18, 4, 13, 'John \"Red\" Hamilton'),
(19, 4, 20, 'George \"Baby Face\" Nelson'),
(20, 4, 21, 'Charles Winstead'),
(21, 4, 22, 'Harry Pierpont'),
(22, 4, 23, 'J. Edgar Hoover'),
(23, 4, 24, 'Carol Slayman'),
(24, 4, 25, 'Harry Pierpont'),
(25, 4, 27, 'Billie Frechette'),
(26, 4, 28, 'Melvin Purvis'),
(27, 4, 30, 'John Dillinger'),
(28, 5, 9, 'Tommy Conlon'),
(29, 5, 31, 'Bryan Callen'),
(30, 5, 32, 'Colt Boyd'),
(31, 5, 33, 'Principal Zito'),
(32, 5, 34, 'Tess Conlon'),
(33, 5, 35, 'Frank Campana'),
(34, 5, 36, 'Brendan Conlon'),
(35, 5, 37, 'Paddy Conlon'),
(41, 6, 39, 'Neo'),
(42, 6, 41, 'Trinity'),
(43, 6, 42, 'Agent Smith'),
(44, 6, 40, 'Morpheus'),
(45, 7, 45, 'Sean'),
(46, 7, 44, 'Will'),
(47, 7, 43, 'Chuckie'),
(48, 7, 46, 'Lambeau'),
(49, 7, 47, 'Krystyn'),
(50, 7, 48, 'Morgan'),
(51, 8, 49, 'Vincent'),
(52, 8, 50, 'Irene'),
(53, 8, 51, 'Jerome'),
(54, 9, 52, 'Tristan Ludlow'),
(55, 9, 53, 'Colonel William Ludlow'),
(56, 9, 54, 'Alfred Ludlow'),
(57, 9, 55, 'Susannah Fincannon'),
(58, 10, 30, 'Donnie'),
(59, 10, 57, 'Lefty'),
(60, 10, 56, 'Sonny'),
(61, 10, 58, 'Nicky'),
(62, 10, 59, 'Paulie'),
(63, 11, 60, 'Deckard'),
(64, 11, 61, 'Batty'),
(65, 11, 62, 'Rachael'),
(66, 12, 63, 'Bobby Sands'),
(67, 12, 67, 'Raymond Lohan'),
(68, 12, 64, 'Gerry\'s Girlfriend'),
(69, 12, 66, 'Gerry Campbell'),
(70, 12, 65, 'Davey Gillen'),
(71, 13, 68, 'Major Konig'),
(72, 13, 51, 'Vassili'),
(73, 13, 69, 'Commisar Danilov'),
(74, 13, 70, 'Tania Chernova'),
(75, 13, 71, 'Nikita Khrushchev'),
(76, 13, 72, 'Koulikov');

-- --------------------------------------------------------

--
-- Table structure for table `seat`
--

CREATE TABLE `seat` (
  `id` int(11) NOT NULL,
  `hall_id` int(11) NOT NULL,
  `seat_type_id` int(11) NOT NULL,
  `row` int(11) NOT NULL,
  `number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seat`
--

INSERT INTO `seat` (`id`, `hall_id`, `seat_type_id`, `row`, `number`) VALUES
(1, 1, 1, 1, '1'),
(2, 1, 1, 1, '2'),
(3, 1, 1, 1, '3'),
(4, 1, 1, 1, '4'),
(5, 1, 1, 1, '5'),
(6, 1, 1, 1, '6'),
(7, 1, 1, 1, '7'),
(8, 1, 1, 1, '8'),
(9, 1, 4, 1, '9'),
(10, 1, 4, 1, '10'),
(11, 1, 1, 2, '1'),
(12, 1, 1, 2, '2'),
(13, 1, 1, 2, '3'),
(14, 1, 1, 2, '4'),
(15, 1, 1, 2, '5'),
(16, 1, 1, 2, '6'),
(17, 1, 1, 2, '7'),
(18, 1, 1, 2, '8'),
(19, 1, 1, 2, '9'),
(20, 1, 1, 2, '10'),
(21, 1, 1, 3, '1'),
(22, 1, 1, 3, '2'),
(23, 1, 5, 3, '3/4'),
(25, 1, 1, 3, '5'),
(26, 1, 1, 3, '6'),
(27, 1, 1, 3, '7'),
(28, 1, 1, 3, '8'),
(29, 1, 1, 3, '9'),
(30, 1, 1, 3, '10'),
(31, 1, 1, 4, '1'),
(32, 1, 1, 4, '2'),
(33, 1, 1, 4, '3'),
(34, 1, 1, 4, '4'),
(35, 1, 1, 4, '5'),
(36, 1, 1, 4, '6'),
(37, 1, 1, 4, '7'),
(38, 1, 1, 4, '8'),
(39, 1, 1, 4, '9'),
(40, 1, 1, 4, '10'),
(41, 1, 1, 5, '1'),
(42, 1, 1, 5, '2'),
(43, 1, 1, 5, '3'),
(44, 1, 1, 5, '4'),
(45, 1, 1, 5, '5'),
(46, 1, 1, 5, '6'),
(47, 1, 5, 5, '7/8'),
(49, 1, 1, 5, '9'),
(50, 1, 1, 5, '10'),
(51, 1, 1, 5, '11'),
(52, 1, 1, 5, '12'),
(53, 1, 2, 6, '1'),
(54, 1, 2, 6, '2'),
(55, 1, 2, 6, '3'),
(56, 1, 2, 6, '4'),
(57, 1, 2, 6, '5'),
(58, 1, 2, 6, '6'),
(59, 1, 2, 6, '7'),
(60, 1, 2, 6, '8'),
(61, 1, 2, 6, '9'),
(62, 1, 2, 6, '10'),
(63, 1, 2, 6, '11'),
(64, 1, 2, 6, '12'),
(65, 1, 2, 7, '1'),
(66, 1, 2, 7, '2'),
(67, 1, 2, 7, '3'),
(68, 1, 2, 7, '4'),
(69, 1, 2, 7, '5'),
(70, 1, 2, 7, '6'),
(71, 1, 2, 7, '7'),
(72, 1, 2, 7, '8'),
(73, 1, 2, 7, '9'),
(74, 1, 2, 7, '10'),
(75, 1, 2, 7, '11'),
(76, 1, 2, 7, '12'),
(77, 2, 1, 1, '1'),
(78, 2, 1, 1, '2'),
(79, 2, 1, 1, '3'),
(80, 2, 1, 1, '4'),
(81, 2, 1, 1, '5'),
(82, 2, 1, 1, '6'),
(83, 2, 1, 1, '7'),
(84, 2, 1, 1, '8'),
(85, 2, 1, 1, '9'),
(86, 2, 1, 1, '10'),
(87, 2, 1, 2, '1'),
(88, 2, 1, 2, '2'),
(89, 2, 1, 2, '3'),
(90, 2, 1, 2, '4'),
(91, 2, 1, 2, '5'),
(92, 2, 1, 2, '6'),
(93, 2, 1, 2, '7'),
(94, 2, 1, 2, '8'),
(95, 2, 1, 2, '9'),
(96, 2, 1, 2, '10'),
(97, 2, 1, 3, '1'),
(98, 2, 1, 3, '2'),
(99, 2, 1, 3, '3'),
(100, 2, 5, 3, '4/5'),
(102, 2, 1, 3, '6'),
(103, 2, 1, 3, '7'),
(104, 2, 1, 3, '8'),
(105, 2, 1, 3, '9'),
(106, 2, 1, 3, '10'),
(107, 2, 1, 4, '1'),
(108, 2, 1, 4, '2'),
(109, 2, 1, 4, '3'),
(110, 2, 1, 4, '4'),
(111, 2, 1, 4, '5'),
(112, 2, 1, 4, '6'),
(113, 2, 1, 4, '7'),
(114, 2, 1, 4, '8'),
(115, 2, 1, 4, '9'),
(116, 2, 1, 4, '10'),
(117, 2, 1, 5, '1'),
(118, 2, 1, 5, '2'),
(119, 2, 1, 5, '3'),
(120, 2, 1, 5, '4'),
(121, 2, 1, 5, '5'),
(122, 2, 1, 5, '6'),
(123, 2, 5, 5, '7/8'),
(125, 2, 1, 5, '9'),
(126, 2, 1, 5, '10'),
(127, 2, 2, 6, '1'),
(128, 2, 2, 6, '2'),
(129, 2, 2, 6, '3'),
(130, 2, 2, 6, '4'),
(131, 2, 2, 6, '5'),
(132, 2, 2, 6, '6'),
(133, 2, 2, 6, '7'),
(134, 2, 2, 6, '8'),
(135, 2, 2, 6, '9'),
(136, 2, 2, 6, '10');

-- --------------------------------------------------------

--
-- Table structure for table `seat_type`
--

CREATE TABLE `seat_type` (
  `id` int(11) NOT NULL,
  `type` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seat_type`
--

INSERT INTO `seat_type` (`id`, `type`, `image`) VALUES
(1, 'normal', 'normal.png'),
(2, 'vip', 'vip.png'),
(3, 'unavailable', 'unavailable.png'),
(4, 'disabled', 'disabled.png'),
(5, 'love', 'love.png'),
(6, 'reserved', 'reserved.png');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `last_login_at` datetime DEFAULT NULL,
  `last_login_ip` varchar(255) DEFAULT NULL,
  `last_seen` datetime DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `confirmed_at` datetime DEFAULT NULL,
  `auth_token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `email`, `username`, `password`, `date_of_birth`, `phone_number`, `image`, `is_superuser`, `date_joined`, `last_login_at`, `last_login_ip`, `last_seen`, `login_count`, `confirmed_at`, `auth_token`) VALUES
(1, 'Miloš', 'Marković', 'milos.dj.markovic@gmail.com', 'clutch_lord', '$pbkdf2-sha256$29000$xDjnvHduTUmp9V6LMaYUIg$H3XW0CGqQKG6ATH.LWxKWzZAIBqvrGZpdMA4t0tlMmg', '1999-01-15', '062/18-17-855', '1.png', 1, '2023-04-30 01:11:03', '2023-05-15 07:16:09', '127.0.0.1', '2023-05-15 08:45:04', 56, '2023-04-30 01:11:03', '$pbkdf2-sha256$29000$fo/x/t/buxcixBjjPEdIiQ$vHxTPCJLpVfAqdrf5xKq8aKbz94/cASpHnsPpBQDfWo'),
(2, 'Miloš', 'Marković', 'milosmarkovicx3@gmail.com', 'diablo', '$pbkdf2-sha256$29000$thZCKIWQEmLsfS8FIOR8Tw$DbfDz7l1aOtebcDG4kcy/NDM/eZ176BAhJyNtmnNMAs', '0000-00-00', 'None', '2.jpg', 0, '2023-05-10 04:11:01', '2023-05-13 02:36:05', '127.0.0.1', '2023-05-13 02:48:14', 3, '2023-05-10 04:16:24', '$pbkdf2-sha256$29000$JGRsbU2ptRYiBGDM.X9v7Q$EwRAQciWvk9oZh/ImjsaskYaB.hlwZzNlCPyF84ISDY');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actor`
--
ALTER TABLE `actor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `image` (`image`);

--
-- Indexes for table `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `genre` (`name`),
  ADD UNIQUE KEY `image` (`image`);

--
-- Indexes for table `hall`
--
ALTER TABLE `hall`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mailing_list`
--
ALTER TABLE `mailing_list`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `movie`
--
ALTER TABLE `movie`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `image` (`poster`);

--
-- Indexes for table `movies_genres`
--
ALTER TABLE `movies_genres`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `projection`
--
ALTER TABLE `projection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `seat`
--
ALTER TABLE `seat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `seat_type`
--
ALTER TABLE `seat_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actor`
--
ALTER TABLE `actor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `hall`
--
ALTER TABLE `hall`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `mailing_list`
--
ALTER TABLE `mailing_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `movie`
--
ALTER TABLE `movie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `movies_genres`
--
ALTER TABLE `movies_genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `projection`
--
ALTER TABLE `projection`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=183;

--
-- AUTO_INCREMENT for table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `seat`
--
ALTER TABLE `seat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;

--
-- AUTO_INCREMENT for table `seat_type`
--
ALTER TABLE `seat_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
