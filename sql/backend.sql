-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2023 a las 03:12:32
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `backend`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignatura`
--

CREATE TABLE `asignatura` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `codigo` varchar(30) NOT NULL,
  `descripcion` text NOT NULL,
  `idprograma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `bancopregunta`
--

CREATE TABLE `bancopregunta` (
  `id` int(11) NOT NULL,
  `idnivel` int(11) NOT NULL,
  `idcomportamiento` int(11) NOT NULL,
  `pregunta` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

CREATE TABLE `cargo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL,
  `idnivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `competencia`
--

CREATE TABLE `competencia` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comportamiento`
--

CREATE TABLE `comportamiento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL,
  `idcompetencia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleevadmon`
--

CREATE TABLE `detalleevadmon` (
  `id` int(11) NOT NULL,
  `idevaluacionadmon` int(11) NOT NULL,
  `idbancopregunta` int(11) NOT NULL,
  `calificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleevadoc`
--

CREATE TABLE `detalleevadoc` (
  `id` int(11) NOT NULL,
  `ideva_doc_asig_est` int(11) NOT NULL,
  `idbancopregunta` int(11) NOT NULL,
  `calificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_evadoc_director`
--

CREATE TABLE `detalle_evadoc_director` (
  `id` int(11) NOT NULL,
  `ideva_doc_director` int(11) NOT NULL,
  `idbancopregunta` int(11) NOT NULL,
  `calificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacionadmon`
--

CREATE TABLE `evaluacionadmon` (
  `id` int(11) NOT NULL,
  `idtrabajador` int(11) NOT NULL,
  `idjefe` int(11) NOT NULL,
  `idcargo` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `periodo` varchar(30) NOT NULL,
  `idtipoevaluacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluaciondoc`
--

CREATE TABLE `evaluaciondoc` (
  `id` int(11) NOT NULL,
  `iddocente` int(11) NOT NULL,
  `periodo` varchar(30) NOT NULL,
  `idtipoevaluacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eva_doc_asig_est`
--

CREATE TABLE `eva_doc_asig_est` (
  `id` int(11) NOT NULL,
  `idestudiante` int(11) NOT NULL,
  `idgrupo` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `idevaluaciondoc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eva_doc_director`
--

CREATE TABLE `eva_doc_director` (
  `id` int(11) NOT NULL,
  `idejefe` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `idevaluaciondoc` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facultad`
--

CREATE TABLE `facultad` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL,
  `idasignatura` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulo`
--

CREATE TABLE `modulo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloxperfil`
--

CREATE TABLE `moduloxperfil` (
  `id` int(11) NOT NULL,
  `idmodulo` int(11) NOT NULL,
  `idperfil` int(11) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE `nivel` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perfil`
--

CREATE TABLE `perfil` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programa`
--

CREATE TABLE `programa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL,
  `idfacultad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoevaluacion`
--

CREATE TABLE `tipoevaluacion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `nombres` varchar(20) NOT NULL,
  `apellido1` varchar(20) NOT NULL,
  `apellido2` varchar(20) NOT NULL,
  `tipodocumento` varchar(20) NOT NULL,
  `identificacion` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `idperfil` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idprograma` (`idprograma`);

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `bancopregunta`
--
ALTER TABLE `bancopregunta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idnivel` (`idnivel`),
  ADD KEY `idcomportamiento` (`idcomportamiento`);

--
-- Indices de la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idnivel` (`idnivel`);

--
-- Indices de la tabla `competencia`
--
ALTER TABLE `competencia`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `comportamiento`
--
ALTER TABLE `comportamiento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idcompetencia` (`idcompetencia`);

--
-- Indices de la tabla `detalleevadmon`
--
ALTER TABLE `detalleevadmon`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idevaluacionadmon` (`idevaluacionadmon`),
  ADD KEY `idbancopregunta` (`idbancopregunta`);

--
-- Indices de la tabla `detalleevadoc`
--
ALTER TABLE `detalleevadoc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ideva_doc_asig_est` (`ideva_doc_asig_est`),
  ADD KEY `idbancopregunta` (`idbancopregunta`);

--
-- Indices de la tabla `detalle_evadoc_director`
--
ALTER TABLE `detalle_evadoc_director`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ideva_doc_director` (`ideva_doc_director`),
  ADD KEY `idbancopregunta` (`idbancopregunta`);

--
-- Indices de la tabla `evaluacionadmon`
--
ALTER TABLE `evaluacionadmon`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idtrabajador` (`idtrabajador`),
  ADD KEY `idjefe` (`idjefe`),
  ADD KEY `idcargo` (`idcargo`),
  ADD KEY `idtipoevaluacion` (`idtipoevaluacion`);

--
-- Indices de la tabla `evaluaciondoc`
--
ALTER TABLE `evaluaciondoc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `iddocente` (`iddocente`),
  ADD KEY `idtipoevaluacion` (`idtipoevaluacion`);

--
-- Indices de la tabla `eva_doc_asig_est`
--
ALTER TABLE `eva_doc_asig_est`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idestudiante` (`idestudiante`),
  ADD KEY `idgrupo` (`idgrupo`),
  ADD KEY `idevaluaciondoc` (`idevaluaciondoc`);

--
-- Indices de la tabla `eva_doc_director`
--
ALTER TABLE `eva_doc_director`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idejefe` (`idejefe`),
  ADD KEY `idevaluaciondoc` (`idevaluaciondoc`);

--
-- Indices de la tabla `facultad`
--
ALTER TABLE `facultad`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idasignatura` (`idasignatura`);

--
-- Indices de la tabla `modulo`
--
ALTER TABLE `modulo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `moduloxperfil`
--
ALTER TABLE `moduloxperfil`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idmodulo` (`idmodulo`),
  ADD KEY `idperfil` (`idperfil`);

--
-- Indices de la tabla `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `perfil`
--
ALTER TABLE `perfil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `programa`
--
ALTER TABLE `programa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `idfacultad` (`idfacultad`);

--
-- Indices de la tabla `tipoevaluacion`
--
ALTER TABLE `tipoevaluacion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD UNIQUE KEY `identificacion` (`identificacion`),
  ADD KEY `idperfil` (`idperfil`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignatura`
--
ALTER TABLE `asignatura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `bancopregunta`
--
ALTER TABLE `bancopregunta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cargo`
--
ALTER TABLE `cargo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `competencia`
--
ALTER TABLE `competencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `comportamiento`
--
ALTER TABLE `comportamiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalleevadmon`
--
ALTER TABLE `detalleevadmon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalleevadoc`
--
ALTER TABLE `detalleevadoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_evadoc_director`
--
ALTER TABLE `detalle_evadoc_director`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluacionadmon`
--
ALTER TABLE `evaluacionadmon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluaciondoc`
--
ALTER TABLE `evaluaciondoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `eva_doc_asig_est`
--
ALTER TABLE `eva_doc_asig_est`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `eva_doc_director`
--
ALTER TABLE `eva_doc_director`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facultad`
--
ALTER TABLE `facultad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `grupo`
--
ALTER TABLE `grupo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulo`
--
ALTER TABLE `modulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `moduloxperfil`
--
ALTER TABLE `moduloxperfil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `nivel`
--
ALTER TABLE `nivel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `perfil`
--
ALTER TABLE `perfil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `programa`
--
ALTER TABLE `programa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipoevaluacion`
--
ALTER TABLE `tipoevaluacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignatura`
--
ALTER TABLE `asignatura`
  ADD CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`idprograma`) REFERENCES `programa` (`id`);

--
-- Filtros para la tabla `bancopregunta`
--
ALTER TABLE `bancopregunta`
  ADD CONSTRAINT `bancopregunta_ibfk_1` FOREIGN KEY (`idnivel`) REFERENCES `nivel` (`id`),
  ADD CONSTRAINT `bancopregunta_ibfk_2` FOREIGN KEY (`idcomportamiento`) REFERENCES `comportamiento` (`id`);

--
-- Filtros para la tabla `cargo`
--
ALTER TABLE `cargo`
  ADD CONSTRAINT `cargo_ibfk_1` FOREIGN KEY (`idnivel`) REFERENCES `nivel` (`id`);

--
-- Filtros para la tabla `comportamiento`
--
ALTER TABLE `comportamiento`
  ADD CONSTRAINT `comportamiento_ibfk_1` FOREIGN KEY (`idcompetencia`) REFERENCES `competencia` (`id`);

--
-- Filtros para la tabla `detalleevadmon`
--
ALTER TABLE `detalleevadmon`
  ADD CONSTRAINT `detalleevadmon_ibfk_1` FOREIGN KEY (`idevaluacionadmon`) REFERENCES `evaluacionadmon` (`id`),
  ADD CONSTRAINT `detalleevadmon_ibfk_2` FOREIGN KEY (`idbancopregunta`) REFERENCES `bancopregunta` (`id`);

--
-- Filtros para la tabla `detalleevadoc`
--
ALTER TABLE `detalleevadoc`
  ADD CONSTRAINT `detalleevadoc_ibfk_1` FOREIGN KEY (`ideva_doc_asig_est`) REFERENCES `eva_doc_asig_est` (`id`),
  ADD CONSTRAINT `detalleevadoc_ibfk_2` FOREIGN KEY (`idbancopregunta`) REFERENCES `bancopregunta` (`id`);

--
-- Filtros para la tabla `detalle_evadoc_director`
--
ALTER TABLE `detalle_evadoc_director`
  ADD CONSTRAINT `detalle_evadoc_director_ibfk_1` FOREIGN KEY (`ideva_doc_director`) REFERENCES `eva_doc_director` (`id`),
  ADD CONSTRAINT `detalle_evadoc_director_ibfk_2` FOREIGN KEY (`idbancopregunta`) REFERENCES `bancopregunta` (`id`);

--
-- Filtros para la tabla `evaluacionadmon`
--
ALTER TABLE `evaluacionadmon`
  ADD CONSTRAINT `evaluacionadmon_ibfk_1` FOREIGN KEY (`idtrabajador`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `evaluacionadmon_ibfk_2` FOREIGN KEY (`idjefe`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `evaluacionadmon_ibfk_3` FOREIGN KEY (`idcargo`) REFERENCES `cargo` (`id`),
  ADD CONSTRAINT `evaluacionadmon_ibfk_4` FOREIGN KEY (`idtipoevaluacion`) REFERENCES `tipoevaluacion` (`id`);

--
-- Filtros para la tabla `evaluaciondoc`
--
ALTER TABLE `evaluaciondoc`
  ADD CONSTRAINT `evaluaciondoc_ibfk_1` FOREIGN KEY (`iddocente`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `evaluaciondoc_ibfk_2` FOREIGN KEY (`idtipoevaluacion`) REFERENCES `tipoevaluacion` (`id`);

--
-- Filtros para la tabla `eva_doc_asig_est`
--
ALTER TABLE `eva_doc_asig_est`
  ADD CONSTRAINT `eva_doc_asig_est_ibfk_1` FOREIGN KEY (`idestudiante`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `eva_doc_asig_est_ibfk_2` FOREIGN KEY (`idgrupo`) REFERENCES `grupo` (`id`),
  ADD CONSTRAINT `eva_doc_asig_est_ibfk_3` FOREIGN KEY (`idevaluaciondoc`) REFERENCES `evaluaciondoc` (`id`);

--
-- Filtros para la tabla `eva_doc_director`
--
ALTER TABLE `eva_doc_director`
  ADD CONSTRAINT `eva_doc_director_ibfk_1` FOREIGN KEY (`idejefe`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `eva_doc_director_ibfk_2` FOREIGN KEY (`idevaluaciondoc`) REFERENCES `evaluaciondoc` (`id`);

--
-- Filtros para la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`idasignatura`) REFERENCES `asignatura` (`id`);

--
-- Filtros para la tabla `moduloxperfil`
--
ALTER TABLE `moduloxperfil`
  ADD CONSTRAINT `moduloxperfil_ibfk_1` FOREIGN KEY (`idmodulo`) REFERENCES `modulo` (`id`),
  ADD CONSTRAINT `moduloxperfil_ibfk_2` FOREIGN KEY (`idperfil`) REFERENCES `perfil` (`id`);

--
-- Filtros para la tabla `programa`
--
ALTER TABLE `programa`
  ADD CONSTRAINT `programa_ibfk_1` FOREIGN KEY (`idfacultad`) REFERENCES `facultad` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`idperfil`) REFERENCES `perfil` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
